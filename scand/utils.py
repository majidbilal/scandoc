from django.shortcuts import redirect, render


def status_change(request, approve=False, image_id=None, model=None):
    if image_id:
        imageset = model.objects.filter(id=image_id)  # To call update
        image = model.objects.filter(id=image_id).first()
        status = image.status
        is_reverted = image.is_reverted
    else:
        return render(request, '403.html', context={'exception': 'Bad request'})

    if approve:
        if is_reverted:
            imageset.update(status=status+1, is_forwarded=True)
        else:
            imageset.update(status=status+1)
        return redirect('dashboard')
    elif not approve:
        imageset.update(status=status-1, is_reverted=True, is_forwarded=False)
        return redirect('dashboard')

    return render(request, '403.html', context={'exception': 'Bad request'})
