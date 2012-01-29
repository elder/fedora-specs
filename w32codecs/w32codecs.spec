# Do not create a debuginfo package
%define  debug_package %{nil}

Name:    w32codecs
Version: 20110131
Release: 2%{?dist}
Summary: MPlayer codecs for all video formats

Group:   System Environment/Libraries
License: Redistributable, no modification permitted
URL:     http://www.mplayerhq.hu
Source0: http://www.mplayerhq.hu/MPlayer/releases/codecs/all-%{version}.tar.bz2

# These codecs doesn't work on x86_64 systems.
ExclusiveArch: %ix86

# easyLife installs this package
Obsoletes:  mplayer-codecs-all

%description
MPlayer codecs for all video formats available. These codecs are also used by
other applications. Install them if you want to watch any video without having
to worry about problems with codecs on your system.

%prep
%setup -q -n all-%{version}
chmod -x README

%build

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_libdir}/codecs
install -pm 644 *.* %{buildroot}%{_libdir}/codecs

# Create symbolic link for compatibility
ln -s %{_libdir}/codecs %{buildroot}%{_libdir}/win32

%files
%defattr(-,root,root,-)
%doc README
%dir %{_libdir}/codecs
%{_libdir}/codecs/*
%{_libdir}/win32

%changelog
* Sun Jun 19 2011 Elder Marco <eldermarco@gmail.com> - 20110131-2
- Removed links under /usr/local
- mplayer-codecs-all marked as obsolete

* Tue Apr 19 2011 Elder Marco <eldermarco@gmail.com> - 20110131-1
- Update to new release 

* Fri Jul 30 2010 Elder Marco <eldermarco@gmail.com> - 20100303-1
 - Update to new codecs package

* Sun Feb 21 2010 Elder Marco <eldermarco@gmail.com> - 20071007-1
- Initial Package
