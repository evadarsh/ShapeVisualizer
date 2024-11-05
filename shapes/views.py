# shapes/views.py

from django.shortcuts import render
from .forms import ShapeCodeForm
from .models import Shape
import traceback

def execute_user_code(code):
    local_vars = {}
    try:
        # Execute the user's code with Shape in the global scope
        exec(code, {"Shape": Shape}, local_vars)

        # Look for a class defined by the user that is a subclass of Shape
        shape_class = None
        for obj in local_vars.values():
            if isinstance(obj, type) and issubclass(obj, Shape) and obj is not Shape:
                shape_class = obj
                break

        if shape_class is None:
            return {"status": "error", "description": "No valid shape class found in the code."}

        # Instantiate the shape object with user-defined parameters
        # Here we can either allow user input through other means
        # or provide some defaults.
        shape_instance = shape_class()  # Instantiate the shape without parameters

        # Call the draw() method to get the CSS for the shape
        css_code = shape_instance.draw() if hasattr(shape_instance, 'draw') else "No draw() method found."

        return {"status": "success", "description": css_code}

    except Exception as e:
        return {"status": "error", "description": traceback.format_exc()}

def shape_view(request):
    form = ShapeCodeForm()
    result = None

    if request.method == 'POST':
        form = ShapeCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            
            # Execute user code and get result
            result = execute_user_code(code)

    return render(request, 'shapes/shape_view.html', {'form': form, 'result': result})
