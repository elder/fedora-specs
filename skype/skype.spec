%define     __strip /bin/true
%define     debug_package %{nil}

Name:     skype
Version:  2.2.0.35
Release:  1%{?dist}
Summary:  Free Internet telephony that just works

Group:    Applications/Communications
License:  Redistributable, no modification permitted
URL:      http://www.skype.com
Source0:  http://download.skype.com/linux/%{name}-%{version}.tar.bz2
Source1:  %{name}.conf

BuildRequires:  dos2unix
BuildRequires:  desktop-file-utils
Requires:       alsa-plugins-pulseaudio(x86-32)
Requires:       dbus-libs(x86-32)
Requires:       freetype(x86-32)
Requires:       qt-x11(x86-32)
Requires:       qt(x86-32)
Requires:       hicolor-icon-theme

%description
Skype is a little piece of software that lets you make free calls
to anyone else on Skype, anywhere in the world. And even though
the calls are free, they are really excellent quality.

 * Make free Skype-to-Skype calls to anyone else, anywhere 
   in the world.
 * Call phones and mobiles at pretty cheap rates per minute.
 * Group chat with up to 100 people or conference call with 
   up to nine others.
 * See who you are talking to with free video calls.
 * Free to download.

By downloading and installing this package, you accept the license
terms of the Skype available at
http://www.skype.com/intl/en-us/legal/eula/

%prep
%setup -q
dos2unix LICENSE
%build
# nope

%install
rm -rf %{buildroot}

# Data
install -dm 755 %{buildroot}%{_datadir}/%{name}/{avatars,sounds}
install -pm 644 avatars/*.png %{buildroot}%{_datadir}/%{name}/avatars/
install -pm 644 sounds/*.wav  %{buildroot}%{_datadir}/%{name}/sounds/                     
        
# Other languages
install -dm 755 %{buildroot}%{_datadir}/%{name}/lang
install -pm 644 lang/*.qm %{buildroot}%{_datadir}/%{name}/lang/

# Conf
install -dm 755 %{buildroot}%{_sysconfdir}/prelink.conf.d
install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/prelink.conf.d
install -dm 755 %{buildroot}%{_sysconfdir}/dbus-1/system.d
install -pm 644 %{name}.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d

# Binary
install -dm 755 %{buildroot}%{_bindir}
install -pm 755 %{name} %{buildroot}%{_bindir}

# Icons
install -dm 755 %{buildroot}%{_datadir}/icons/hicolor
for size in 16x16 32x32 48x48; do
    install -Dpm 644 icons/SkypeBlue_${size}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done

# Encoding key in group "Desktop Entry" is deprecated
%{__install} -dm 755 %{buildroot}%{_datadir}/applications
desktop-file-install --remove-key=Encoding \
    --dir %{buildroot}%{_datadir}/applications skype.desktop

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor --quiet || :
fi

if [ -x %{_bindir}/update-desktop-database ]; then
    %{_bindir}/update-desktop-database --quiet ||:
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor --quiet || :
fi

if [ -x %{_bindir}/update-desktop-database ]; then
    %{_bindir}/update-desktop-database --quiet ||:
fi 

%files 
%defattr(-,root,root,-)
%doc LICENSE README
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/%{name}.desktop
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/skype.conf
%config(noreplace) %{_sysconfdir}/prelink.conf.d/skype.conf

%changelog
* Wed Jun 29 2011 - Elder Marco <eldermarco@gmail.com> - 2.2.0.35-1
- Update to new version.

* Sat Apr 09 2011 - Elder Marco <eldermarco@gmail.com> - 2.2.0.25-1
- Update to new version.

* Sat Feb 26 2011 - Elder Marco <eldermarco@gmail.com> - 2.1.0.81-1
- Initial package
- Description is the same of the skype rpm file on skype website.
