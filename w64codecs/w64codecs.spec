%define  debug_package %{nil}
%global  _lib32dir     %{_prefix}/lib

Name:    w64codecs
Version: 20071007
Release: 2%{?dist}
Summary: MPlayer proprietary codecs binary for x86_64 systems

Group:   System Environment/Libraries
License: Redistributable, no modification permitted
URL:     http://www.mplayerhq.hu
Source0: http://www.mplayerhq.hu/MPlayer/releases/codecs/essential-amd64-%{version}.tar.bz2

ExclusiveArch: x86_64

Requires: libstdc++ >= 4.1.1

%description
This package contains the "Win32" codec binaries for the x86_64 architectures, 
required for the decompression of video formats that have no open source 
alternative.

%prep
%setup -q -n essential-amd64-%{version}

%build

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_libdir}/codecs
install -m 644 *.* %{buildroot}%{_libdir}/codecs/

# Create symbolic links for compatibility
install -dm 755 %{buildroot}%{_lib32dir}
ln -s    %{_libdir}/codecs %{buildroot}%{_lib32dir}/codecs
ln -s    %{_libdir}/codecs %{buildroot}%{_lib32dir}/win32

%files
%defattr(-,root,root,-)
%doc README
%dir %{_libdir}/codecs
%{_libdir}/codecs/*
%{_lib32dir}/codecs
%{_lib32dir}/win32

%changelog
* Thu Jun 23 2011 Elder Marco <eldermarco@gmail.com> - 20071007-2
- Removed symlinks under /usr/local

* Fri Jul 30 2010 Elder Marco <eldermarco@gmail.com> - 20071007-1
- Initial Package based on Medibuntu package
