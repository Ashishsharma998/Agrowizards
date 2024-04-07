from django.shortcuts import render

from django.http import HttpResponse
import pandas as pd;
import matplotlib.pyplot as plt;

import os

import io
import base64


# Create your views here.

def pcidata(request):
    file_path = os.path.join(os.path.dirname(__file__), 'mydata', 'crop_yield.csv')
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    data = pd.read_csv(file_path)
    pci=data['Crop'].value_counts()
    pci_ind = pci.index
    pci_val = pci.values
    
    context1 = {
        'pci': pci, 
        'pci_ind': pci_ind,
        'pci_val': pci_val
    }

    # plot the graph
    # Create a plot

    plt.figure(figsize=(30, 50))
    plt.bar(pci_ind, pci_val, color=['r', 'b'])
    plt.xlabel("Crops Name", size=50)
    plt.xticks(size=30, rotation=90)
    plt.yticks(size=30)
    plt.ylabel("No of Times It Grown", size=50)
    plt.title("Crop vs No of Times It Grown", size=40)
    
    # Save the plot to an in-memory buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Convert the buffer to a base64-encoded string
    image_base64 = buffer.getvalue()
    image_base64 = base64.b64encode(image_base64).decode('utf-8')
    
    # Pass the image URL to the template
    context2 = {
        'image_base64': 'data:image/png;base64,' + image_base64
    }

    # list of popular crops of india with respect to seasons
    pci_ind = data[data['Season'] == 'Rabi']['Crop']
    # states  with their respective  crops
    mpcos=data.groupby('State')['Crop'].sum()
    context3 = {
        'mpcos':mpcos
    }

    return render(request, template_path, {'context1': context1, 'context2': context2, 'context3':context3})

def home(request):
    return HttpResponse("Hello, World!")
