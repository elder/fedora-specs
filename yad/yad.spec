Name:      yad
Version:   0.16.3
Release:   1%{?dist}
Summary:   Display graphical dialogs from shell scripts or command line

Group:     Applications/System
License:   GPLv3+
URL:       http://yad.googlecode.com
Source0:   http://yad.googlecode.com/files/%{name}-%{version}.tar.xz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk3-devel >= 2.91.0
BuildRequires:  desktop-file-utils
BuildRequires:  intltool >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  gettext

%description
Yad (yet another dialog) is a fork of zenity with many improvements, such as
custom buttons, additional dialogs, pop-up menu in notification icon and more.

%prep
%setup -q

%build
%configure --enable-icon-browser --with-gtk=gtk3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%find_lang %{name}

# Encoding key in group "Desktop Entry" is deprecated.
# Place the menu entry for yad-icon-browser under "Utilities".
desktop-file-install --remove-key Encoding     \
    --remove-category Development              \
    --add-category    Utility                  \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}-icon-browser.desktop

%clean
rm -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog AUTHORS COPYING NEWS THANKS TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-icon-browser
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}-icon-browser.desktop
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Dec 06 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.16.3-1
- Update to new version

* Tue Nov 15 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.15.2-1
- Update to new version
- Removed condition %%if 0%%{?fedora} < 15.

* Sun Nov 06 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.15.1-1
- Update to new version

* Sun Oct 16 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.15.0-1
- Update to new version

* Thu Sep 08 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.14.2-1
- Update to new version

* Sat Aug 13 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.13.0-1
- New upstream release

* Fri Jul 08 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.4-2
- Menu entry for yad-icon-browser placed under "Utilities"

* Fri Jul 01 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.4-1
- Update to 0.12.4
- Removed patch to fix FSF address (now, it's not necessary)

* Tue Jun 28 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.3-3
- Added patch to fix FSF address (from upstream)

* Sun Jun 26 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.3-2
- Edited spec file to conform to the fedora guidelines

* Thu Jun 25 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.12.3-1
- New upstream release

* Sat May 21 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.11.0-1
- New upstream release

* Sun May 01 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.10.2-1
- New upstream release

* Tue Apr 12 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.10.1-1
- New upstream release

* Wed Mar 30 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.10.0-1
- New upstream release
- Added build option --disable-deprecated

* Sun Mar 13 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.1-1
- New upstream release
- Added desktop-file-utils as BuildRequires.
- Removed clean section and BuildRoot tag (not required any more).
- Removed Encoding key from .desktop file.

* Tue Mar 08 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.0-1
- Initial package
