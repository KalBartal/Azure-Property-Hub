from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import PropertyForm, PropertySearchForm
from .models import Property


@login_required
@permission_required('properties.add_property')
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property created successfully!')
            return redirect('properties:property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/create_property.html', {'form': form})


@login_required
@permission_required('properties.change_property')
def edit_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property updated successfully!')
            return redirect('properties:property_detail', property_id=property.id)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties/edit_property.html', {'form': form, 'property': property})


@login_required
@permission_required('properties.delete_property')
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        messages.success(request, 'Property deleted successfully!')
        return redirect('properties:property_list')
    return render(request, 'properties/property_delete.html', {'property': property})


@login_required
@permission_required('properties.add_property')
def upload_property_photo(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property photo uploaded successfully!')
            return redirect('properties:property_detail', property_id=property.id)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties/upload_property_photo.html', {'form': form, 'property': property})


def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})


def property_list(request):
    form = PropertySearchForm(request.GET)
    properties = Property.objects.all()

    if form.is_valid():
        search = form.cleaned_data.get('search')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if search:
            properties = properties.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(address__icontains=search)
            )

        if min_price:
            properties = properties.filter(price__gte=min_price)

        if max_price:
            properties = properties.filter(price__lte=max_price)

    return render(request, 'properties/property_list.html', {'properties': properties, 'form': form})
