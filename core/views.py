from django.shortcuts import render, HttpResponseRedirect
from .forms import EmailForm, EmailModelForm

from .models import Join
import uuid

def get_ip(request):
	try:
		ip_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if ip_forward:
			ip = ip_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip =""

	return ip

#creating logic for generating unique reference id
def get_ref_id():
	# x = uuid.uuid4()
	# ref_id = str(x)
	# ref_id = ref_id[:15]
	# ref_id = ref_id.replace("-", "")
	# ref_id = ref_id.lower()
	# return ref_id
	# simply the above logic in one line
	ref_id = str(uuid.uuid4())[:15].replace("-","").lower()
	#lets take only unique ref_id
	try:
		ref_id_exist = Join.objects.get(ref_id = ref_id)
		get_ref_id()
	except:
		return ref_id


# Create your views here.
def share(request, ref_id):
	context = {'ref_id': ref_id}
	return render(request, 'share.html', context)


# Create your views here.
def index(request):

	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
	except:
		obj = None	

	form = EmailModelForm(request.POST or None)
	if form.is_valid():
		# new_join = form.save(commit=False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_old.ip_address = get_ip(request)
			new_join_old.ref_id = get_ref_id()
			if not obj==None:
				new_join_old.friend=obj

			new_join_old.save()
			print Join.objects.filter(friend=obj).count()

		return HttpResponseRedirect("/%s"%(new_join_old.ref_id))
	
	context = {'form': form,}
	return render(request, 'index.html', context)