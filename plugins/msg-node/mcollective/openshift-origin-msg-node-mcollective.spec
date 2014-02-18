%if 0%{?fedora}%{?rhel} <= 6
    %global scl ruby193
    %global scl_prefix ruby193-
    %global vendor_ruby /opt/rh/%{scl}/root/usr/share/ruby/vendor_ruby/
    %global mco_agent_root /opt/rh/%{scl}/root/usr/libexec/mcollective/mcollective/agent/
    %global update_yaml_root /opt/rh/ruby193/root/usr/libexec/mcollective/
%else
    %global vendor_ruby /usr/share/ruby/vendor_ruby/
    %global mco_agent_root /usr/libexec/mcollective/mcollective/agent/
    %global update_yaml_root /usr/libexec/mcollective/
%endif

Summary:       M-Collective agent file for openshift-origin-msg-node-mcollective
Name:          openshift-origin-msg-node-mcollective
Version: 1.21.0
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      %{?scl:%scl_prefix}rubygems
Requires:      %{?scl:%scl_prefix}rubygem-open4
Requires:      %{?scl:%scl_prefix}rubygem-json
Requires:      rubygem-openshift-origin-node
Requires:      %{?scl:%scl_prefix}mcollective
Requires:      %{?scl:%scl_prefix}facter
Requires:      openshift-origin-msg-common
BuildArch:     noarch

%description
mcollective communication plugin

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{mco_agent_root}
mkdir -p %{buildroot}%{vendor_ruby}facter
mkdir -p %{buildroot}/etc/cron.minutely
mkdir -p %{buildroot}/usr/libexec/mcollective

cp -p src/openshift.rb %{buildroot}%{mco_agent_root}
cp -p facts/openshift_facts.rb %{buildroot}%{vendor_ruby}facter/
cp -p facts/openshift-facts %{buildroot}/etc/cron.minutely/
cp -p facts/update_yaml.rb %{buildroot}%{update_yaml_root}

%files
%{mco_agent_root}openshift.rb
%{vendor_ruby}facter/openshift_facts.rb
%attr(0700,-,-) %{update_yaml_root}/update_yaml.rb
%attr(0700,-,-) %config(noreplace) /etc/cron.minutely/openshift-facts

%changelog
* Sun Feb 16 2014 Adam Miller <admiller@redhat.com> 1.20.3-1
- Bug 1064580 - Keep gear boosted during create (jhonce@redhat.com)

* Mon Feb 10 2014 Adam Miller <admiller@redhat.com> 1.20.2-1
- Merge pull request #4682 from danmcp/cleaning_specs
  (dmcphers+openshiftbot@redhat.com)
- Cleaning specs (dmcphers@redhat.com)
- Merge pull request #4679 from danmcp/cleanup_mco_ddl
  (dmcphers+openshiftbot@redhat.com)
- Cleanup mco ddl (dmcphers@redhat.com)
- Merge pull request #4616 from brenton/deployment_dir1
  (dmcphers+openshiftbot@redhat.com)
- Merge pull request #4671 from rajatchopra/master
  (dmcphers+openshiftbot@redhat.com)
- fix the occluded haproxy gear's frontend upon move when two proxy gears clash
  on a node (rchopra@redhat.com)
- Fix for bug 1060760: Missing variable assignment for exception
  (abhgupta@redhat.com)
- Insure --with-initial-deployment-dir defaults to true in case the args isn't
  supplied. (bleanhar@redhat.com)
- Merge pull request #4624 from ironcladlou/dev/syslog
  (dmcphers+openshiftbot@redhat.com)
- Platform logging enhancements (ironcladlou@gmail.com)
- First pass at avoiding deployment dir create on app moves
  (bleanhar@redhat.com)

* Thu Jan 30 2014 Adam Miller <admiller@redhat.com> 1.20.1-1
- Card #185: sending app alias to all web_proxy gears (abhgupta@redhat.com)
- bump_minor_versions for sprint 40 (admiller@redhat.com)

* Thu Jan 23 2014 Adam Miller <admiller@redhat.com> 1.19.8-1
- Merge pull request #4568 from danmcp/bug1049044
  (dmcphers+openshiftbot@redhat.com)
- Node Platform - Optionally generate application key (jhonce@redhat.com)
- Bug 1055371 (dmcphers@redhat.com)
- Bug 1056716 - Agent ignoring RuntimeError (jhonce@redhat.com)

* Wed Jan 22 2014 Adam Miller <admiller@redhat.com> 1.19.7-1
- Bug 1056480 - Removed random character in code (jhonce@redhat.com)

* Tue Jan 21 2014 Adam Miller <admiller@redhat.com> 1.19.6-1
- Merge pull request #4534 from jwhonce/bug/1054825
  (dmcphers+openshiftbot@redhat.com)
- Bug 1054825 - Return better error message for resources exhausted
  (jhonce@redhat.com)

* Mon Jan 20 2014 Adam Miller <admiller@redhat.com> 1.19.5-1
- Bug 1044223 (dmcphers@redhat.com)

* Fri Jan 17 2014 Adam Miller <admiller@redhat.com> 1.19.4-1
- Allow multiple keys to added or removed at the same time (lnader@redhat.com)

* Thu Jan 09 2014 Troy Dawson <tdawson@redhat.com> 1.19.3-1
- Card online_node_319 - Add quota check to git push (jhonce@redhat.com)
- Fix for bug 1047957 (abhgupta@redhat.com)
- Bug 1045995 - Fix get_gears node implementation (rpenta@redhat.com)