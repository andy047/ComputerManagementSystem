from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from report.forms import ReportForm
from report.models import Report


def reports(request):

    reports = {'reports':Report.objects.filter(is_actived=True)}
    return render(request,'reports.html',reports)


def closed_reports(request):
    reports = {'reports':Report.objects.filter(is_actived=False)}
    return render(request,'reports.html',reports)


def new_report(request):

    if request.method=='POST':
        objReportForm = ReportForm(request.POST)
        if objReportForm.is_valid():
            objReportForm.save()
            return redirect('reports')
    else:

        objReportForm = ReportForm()
        reportForm = {'reportForm': objReportForm}
        return render(request, 'new_report.html',reportForm)

def edit_report(request,id):
    report = get_object_or_404(Report,pk=id)
    if request.method=='POST':
        report_form = ReportForm(request.POST,instance=report)
        if report_form.is_valid():
            report_form.save()
            return redirect('reports')
    else:
        report_form = {'report_form':ReportForm(instance=report)}
        return render(request,'edit_report.html',report_form)

def delete_report(request,id):
    report = get_object_or_404(Report,pk=id)
    report.delete()
    return redirect('reports')
