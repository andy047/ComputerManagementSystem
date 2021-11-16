from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView,DeleteView,ListView,UpdateView #TODAS ESTAS CLASES HEREDAN DE LA CLASE VIEW

from django.urls import reverse_lazy


"""
EJEMPLO DE LA CLASE VIEW MAS O MENOS COMO ESTA DEFINIDO:

SOLO HAY QUE INDICAR BASICAMENTE 
model = Employee
template_name = list_employees

template_name = edit_employee, etc

class View():
  

    dispath : verificar el metodo de la solicitud http(si es GET o POST)
    EJEMPLO DE COMO ESTARA DEFINIDO 
    def post(self,*args,**kwargs)
    
    http_not_allowed : 
    
    def get_context_data(self):
        context = {}
        context['queryset']=self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.all()#aqui remplazaria model por Employee
        
    def get_templates_names():
        return self.template_name
        
    def get(self,request,*args,**kwargs)
        return render(request,self.get_templates_names(),self.get_context_data())
        
    

"""


class EmployeeList(ListView):
    model=Employee
    
    #el diccionario empleados a mostrar en html por default es object_list
    template_name = 'list_employees.html'
    
    
    
    #si quisiera reemplazar la consulta o customizarla, remplazariamos la funcion que hereda de ListView
    def get_queryset(self):
        return self.model.objects.all()[:2]#limitamos la lista solo a dos
 

class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'new_employee.html' # la variable a definir en el html se llama {{form}}
    success_url = reverse_lazy('index')
    
class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'edit_employee.html'
    success_url = reverse_lazy('index')
    
class EmployeeDelete(DeleteView):
    model = Employee
    #hay que crear un html con este nombre, el mismo se debe crear un form con metodo POST
    #y un boton para confirmar la eliminacion del registro y otro cancelar con tab <a> que redireccione a index
    #nombre de la variable se llama object en caso de mostrar registro en el html
    template_name = 'delete_employee.html'
    success_url = reverse_lazy('index')
    
