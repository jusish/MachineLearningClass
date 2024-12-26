# def create_vehicle(request):
#     if request.method == 'POST':
#         form = VehicleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('vehicle_list')
#         else:
#             form = VehicleForm()
            
#         return render(request, 'vehicle_form.html', {'form': form})
    
    
    


# def vehicle_list(request):
#     vehicles = Vehicle.objects.all()
#     return render(request, 'vehicle_list.html', {'vehicles': vehicles})

# def vehicle_list_paginated(request):
#     vehicle_query_set = Vehicle.objects.all()
#     paginator = Paginator(vehicle_query_set, 1000)
#     page_number = request.GET.get('page', 1)
#     vehicle_page = paginator.get_page(page_number)
#     return render(request, 'vehicle_list.html', {'vehicle_page': vehicle_page})




# frequency encoding

import pandas as pd

data = {'color' : ["red", "green", "blue", "red", "green"]}
df = pd.DataFrame(data)

freq = df['color'].value_counts(normalize=True)

df['color_freq'] = df['color'].map(freq)

df = df.drop('color', axis=1)


print(df)



