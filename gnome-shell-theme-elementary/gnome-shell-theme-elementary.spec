%global src_name   gnome_shell___elementary_by_half_left-d45raik
%global theme_name elementary
%global theme      Elementary

# Platform dependent constants
# The source contains 2 zip's: one for gnome 3.0 and one for gnome 3.2
%if 0%{?fedora} < 16
%global     shell_ver  3.0
%global     theme_zip  %{theme}
%else
%global     shell_ver  3.2
%global     theme_zip  %{theme}-3.2
%endif

Name:       gnome-shell-theme-%{theme_name}
Version:    %{shell_ver}
Release:    2%{?dist}
Summary:    The %{theme} gnome-shell theme
Group:      User Interface/Desktops

License:    GPLv3 and LGPLv2
URL:        http://half-left.deviantart.com/art/GNOME-Shell-Elementary-251536124
Source0:    http://www.deviantart.com/download/251536124/%{src_name}.zip

Requires:   gnome-shell-extension-user-theme
Requires:   gnome-shell >= %{shell_ver}
BuildArch:  noarch

%description
The %{theme} gnome-shell theme created by half_left

%prep
%setup -q -c
unzip %{theme_zip}.zip

%build
# nothing to build

%install
mkdir -p -m755 %{buildroot}/%{_datadir}/themes/%{theme}/gnome-shell

# put the theme files into some data dir
cp -pr %{theme_zip}/gnome-shell/* \
     %{buildroot}%{_datadir}/themes/%{theme}/gnome-shell

# delete backup files (*~)
find %{buildroot} -name *~ -type f -exec rm -f '{}' \;

# Remove LICENSE file from BUILDROOT
find %{buildroot} -name LICENSE -type f -exec rm -f '{}' \;

%files
%doc %{theme_zip}/gnome-shell/LICENSE
%dir %{_datadir}/themes/%{theme}
%{_datadir}/themes/%{theme}/*

%changelog
* Mon Oct 31 2011 Elder Marco <eldermarco@fedoraproject.org> - 3.2-2
- Fixed problem with the name of the dependency

* Thu Oct 27 2011 Elder Marco <eldermarco@fedoraproject.org> - 3.2-1
- Update to work on gnome shell 3.0 and gnome-shell 3.2.
- Thanks to Tim Lauridsen.

* Sat Aug 13 2011 Elder Marco <eldermarco@fedoraproject.org> - 1.1-1
- Using patch to fix the version of the theme:
    http://comments.deviantart.com/1/251536124/2144385341

* Sun Jul 02 2011 Elder Marco <eldermarco@fedoraproject.org> - 1.0-2
- Fixed the license field

* Sat Jul 02 2011 Elder Marco <eldermarco@fedoraproject.org> - 1.0-1
- Initial package based on Tim Lauridsen's spec file (Orta theme)
