%global    appname      pidgin
%global    pluginname   gtalk-shared-status

Name:      %{appname}-%{pluginname} 
Version:   0.1.4 
Release:   1%{?dist}
Summary:   Google shared status compatibility plugin for pidgin

Group:     Applications/Internet
License:   GPLv3
URL:       http://www.siorarina.net/gtalk-shared-status/
Source0:   http://www.siorarina.net/gss/src/%{pluginname}-%{version}.src.tar.gz

BuildRequires:  pidgin-devel >= 2.7.1
BuildRequires:  libpurple-devel >= 2.7.1

Requires: pidgin

%description
Adds Google Shared Status compatibility that permit to set the status for all 
the resources connected. This allows to go Invisible.

%prep
%setup -q -n %{pluginname}-%{version}

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -dm 755 %{buildroot}%{_libdir}/%{appname}
install  -m 755 %{pluginname}.so %{buildroot}%{_libdir}/%{appname}

%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING INSTALL 
%{_libdir}/%{appname}/%{pluginname}.so

%changelog
* Tue Apr 19 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.1.4-1
- Initial Package
