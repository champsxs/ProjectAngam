              app                  glean_client_info#app_build#       	                 20211103134640       glean_client_info#app_channel       	                 release%       glean_client_info#app_display_version       	                 94.0.1       glean_client_info#architecture       	                 x86_64       glean_client_info#os       	                 Windows       glean_client_info#os_version       	                 10.0       user    
              glean_client_info#client_id9       	0       	   $       14747fd6-77c0-44f7-9e2f-8d6c8676ccc7        glean_client_info#first_run_date<       	3          #       2020-12-18T22:01:53.129062100+01:00   %       glean_internal_info#baseline#sequence       	            "       glean_internal_info#baseline#start<       	3          #       2022-01-03T22:33:18.227983900+01:00          glean_internal_info#dirtybit       	            +       glean_internal_info#fog-validation#sequence       	          `  (       glean_internal_info#fog-validation#start<       	3          #       2021-04-24T18:44:23.509685700+02:00   $       glean_internal_info#metrics#sequence       	          %   !       glean_internal_info#metrics#start<       	3          #       2022-01-04T04:00:00.009883800+01:00   &       glean_internal_info#mps.last_sent_time<       	3          #       2022-01-03T17:19:13.344625400+01:00          ping           2       baseline#glean.validation.pings_submitted/baseline       	             1       baseline#glean.validation.pings_submitted/metrics       	                    metrics#fog.ipc.buffer_sizes=       	4                 O                   `T      ??lX???       metrics#fog.ipc.flush_durations      	                9+            ??            ?                          ڿ            V            ?_
                                        \?            '?            X            '?            ?/                   p@4    {Q}<?r??0       metrics#glean.validation.pings_submitted/metrics       	                                                                                                                                                                                                                                                                                                                                                                                                                                                                         n render(request, 'users/profile.html', context )

def userAccount(request, username=None):
    if username:
        print("sxssxssxs")
        profile = Profile.objects.get(username=username)
    else:
        profile = request.user.profile
    projects = profile.projects_set.all()
    form = ProfileForm(instance=profile)
    if request.method == 'POST':    
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    context = {'profile': profile, 'projects': projects, 'form': form}
    return render(request, 'users/account.html', context )
    
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)