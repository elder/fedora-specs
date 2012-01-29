%global   src_name     cwp_su_all
%global   src_version  43R1
%global   _optdir      /opt

Name:      seismicunix
Version:   43.1 
Release:   1%{?dist}
Summary:   Open Source software for seismic research and processing

Group:     Applications/Engineering 
License:   BSD 
URL:       http://www.cwp.mines.edu/cwpcodes/ 
Source0:   ftp://ftp.cwp.mines.edu/pub/cwpcodes/%{src_name}_%{src_version}.tgz
Source1:   %{name}.sh
Source2:   %{name}.csh
Patch0:    %{name}-%{version}-makefile-config.patch
Patch1:    %{name}-%{version}-no-questions.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_n} -n)

BuildRequires:  libXmu-devel
BuildRequires:  libXi-devel
BuildRequires:  freeglut-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  lesstif-devel
BuildRequires:  ed
BuildRequires:  gcc-gfortran
Requires:   freeglut
Requires:   lesstif
Requires:   lesstif-mwm

%description
The CWP/SU: Seismic Un*x is an open source seismic utilities package supported
by the Center for Wave Phenomena (CWP) at the Colorado School of Mines (CSM).
The package provides an instant seismic research and processing environment for
users running on all Unix and Unix-like operating systems, which include the
operating systems whose names begin in "U" and end in "X", Mac OS X, Linux,Free
BSD Unix, and the Cygwin32 system for Windows PCs.

%prep
%setup -q -c
cd src
 
%patch0 -p1
%patch1 -p1

%build
export CWPROOT="%{_builddir}/%{name}-%{version}"
cd src

# These codes are essential. Please, don't change anything
# below.
make install        # Basic set of code
make xtinstall      # X-toolkit applications

# The rest are nonessential. You can comment these lines, if
# you want.
make finstall       # Fortran codes
make mglinstall     # Mesa/OpenGL items
make xminstall      # Motif application
make utils          # libcwputils
make sfinstall      # Sfio materials and SEGDREAD

%install
rm -rf %{buildroot}
cd %{_builddir}/%{name}-%{version}

# Create the installation directory
mkdir -p "%{buildroot}%{_optdir}/%{name}"

# Binary files, libraries and include headers
cp -pr bin/ lib/ include/  "%{buildroot}%{_optdir}/%{name}/"

# Source Code and others
mkdir -p "%{buildroot}%{_optdir}/%{name}/src"
find src/* -maxdepth 0 -type d \
    -exec cp -pr '{}' %{buildroot}%{_optdir}/%{name}/src/ \;
rm -rf %{buildroot}%{_optdir}/%{name}/src/configs \
       %{buildroot}%{_optdir}/%{name}/src/Portability

# Environment Variables
install -d -m755 "%{buildroot}/etc/profile.d"
install -m755 "%{SOURCE1}" "%{buildroot}/etc/profile.d/"
install -m755 "%{SOURCE2}" "%{buildroot}/etc/profile.d/"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc src/LEGAL_STATEMENT src/ACKNOWLEDGEMENTS
%{_optdir}/%{name}
%{_sysconfdir}/profile.d/%{name}.*

%changelog
* Fri Jan 28 2012 Elder Marco <eldermarco@fedoraproject.org> - 43.1-1
- Initial package
