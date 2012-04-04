%global uuid remove-accessibility-icon@martin-weusten.de

Name:      gnome-shell-extension-remove-accessibility-icon
Version:   20111008
Release:   3%{?dist}
Summary:   A gnome-shell extensions for removing the accessibility icon

Group:     User Interface/Desktops
License:   BSD
URL:       http://martin-weusten.de/projects/gnomeshell-extensions/remove-accessibility-icon/
Source0:   http://martin-weusten.de/wp-content/uploads/2011/05/remove-accessibility-icon%{version}-1019.tar.gz
Patch0:    gnome-3.4.patch
BuildArch: noarch

Requires:  gnome-shell >= 3.2.0

%description
This simple extension does nothing more than to remove the accessibility
icon in the top right corner of the GNOME panel.


%prep
%setup -q -n %{uuid}

%patch0 -p1

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json,stylesheet.css} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/


%files
%defattr(-,root,root,-)
%doc COPYING README
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Sun Apr 01 2012 Elder Marco <eldermarco@fedoraproject.org> - 20111008-3
- Workaround to fix problem with gnome-shell 3.4

-* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111008-2
-- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Elder Marco <eldermarco@fedoraproject.org> - 20111008-1
- Update to work with gnome-shell >= 3.2.0

* Sat Jun 04 2011 Fabian Affolter <fabian@bernewireless.net> - 20110603-1
- README and COPYING added
- License is Modified BSD License

* Thu Jun 02 2011 Fabian Affolter <fabian@bernewireless.net> - 20110529-1
- Initial package for Fedora
