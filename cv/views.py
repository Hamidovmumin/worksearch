from django.shortcuts import render,redirect
from cv.forms import Step1Form, Step2Form, Step3Form


# Create your views here.
def resume_step(request):
    # step = int(step)
    # form = None
    # width=0
    #
    # if step == 1:
    #     form = Step1Form(request.POST or None)
    #     width=14
    # elif step == 2:
    #     form = Step2Form(request.POST or None)
    #     width=28
    # elif step == 3:
    #     form = Step3Form(request.POST or None)
    #     width=42
    # else:
    #     return redirect('cv:cv', step=1)
    #
    # if request.method == 'POST' and form.is_valid():
    #
    #     return redirect('cv:cv', step=step+1)
    #
    # prev_step = step - 1 if step > 1 else 1
    # next_step = step + 1 if step < 7 else 7
    # steps = {
    #     1: "Vəzifə",
    #     2: "Məlumatlar",
    #     3: "Təhsil",
    #     4: "İş təcrübəsi",
    #     5: "Təsvir",
    #     6: "Əlaqə",
    #     7: "Elan növü",
    # }
    #
    # completed_steps = [i for i in range(1, 8) if request.session.get(f'step_{i}')]
    # context = {
    #     'form': form,
    #     'step': step,
    #     'total_steps': 7,
    #     'completed_steps': completed_steps,
    #     'steps': steps,
    #     'prev_step': prev_step,
    #     'width': width,
    #
    # }

    step = int(request.GET.get("step", 1))

    steps = {
        1: "Vəzifə",
        2: "Məlumatlar",
        3: "Təhsil",
        4: "İş təcrübəsi",
        5: "Təsvir",
        6: "Əlaqə",
        7: "Elan növü",
    }

    if request.method == "POST":
        # əvvəlki dataları saxla
        request.session[f"step_{step}"] = request.POST.dict()

        # növbəti step
        return redirect(request.path + f"?step={step + 1}",step=step+1)

    # if step > 1 and f"step_{step - 1}" not in request.session:
    #     return redirect(request.path + "?step=1")

    completed_steps = [i for i in range(1, 8) if request.session.get(f'step_{i}')]

    context = {
        "step": step,
        "completed_steps": completed_steps,
        'steps': steps,
    }

    return render(request, 'cv/cv.html',context)