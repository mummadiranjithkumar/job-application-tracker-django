from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm


# List all job applications

def job_list(request):
    jobs = JobApplication.objects.all().order_by('-application_date')
    return render(request, 'applications/job_list.html', {'jobs': jobs})


# Create a new job application

def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'applications/job_form.html', {'form': form, 'title': 'Add Job Application'})


# Update an existing job application

def job_update(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'applications/job_form.html', {'form': form, 'title': 'Edit Job Application'})


# Delete a job application

def job_delete(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'applications/job_confirm_delete.html', {'job': job})

