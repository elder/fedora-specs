%global src_name   gnome_shell___elementary_by_half_left-d45raik
%global theme_name elementary
%global theme      Elementary

# Platform dependent constants
# The source contains 2 zip's: one for gnome 3.0 and one for gnome 3.2
%if 0%{?fedora} < 17
%global     shell_ver  3.2
%global     theme_dir  %{theme}-3.2
%else
%global     shell_ver  3.4
%global     theme_dir  %{theme}-3.4
%endif

Name:       gnome-shell-theme-%{theme_name}
Version:    %{shell_ver}
Release:    1%{?dist}
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

%build
# nothing to build

%install
mkdir -p -m755 %{buildroot}/%{_datadir}/themes/%{theme}/gnome-shell

# put the theme files into some data dir
cp -pr %{theme_dir}/gnome-shell/* \
     %{buildroot}%{_datadir}/themes/%{theme}/gnome-shell

# delete backup files (*~)
find %{buildroot} -name *~ -type f -exec rm -f '{}' \;

# Remove LICENSE file from BUILDROOT
find %{buildroot} -name LICENSE -type f -exec rm -f '{}' \;

%files
%doc %{theme_dir}/gnome-shell/LICENSE
%dir %{_datadir}/themes/%{theme}
%{_datadir}/themes/%{theme}/*

%changelog
* Wed Apr 04 2012 Elder Marco <eldermarco@fedoraproject.org> - 3.4-1
- Update to work on gnome shell 3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

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
