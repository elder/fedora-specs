Name:      msttcorefonts
Version:   1.0
Release:   1%{?dist}
Summary:   Microsoft TrueType core fontes for the web

Group:     User Interface/X
License:   Redistributable, no modification permitted
URL:       http://corefonts.sf.net
Source0:   %{name}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:  noarch

%description
This package allows for easy installation of the Microsoft True Type Core Fonts
for the Web including:

   * Andale Mono;
   * Arial Black;
   * Arial (Bold, Italic, Bold Italic);
   * Comic Sans MS (Bold);  
   * Courier New (Bold, Italic, Bold Italic);
   * Georgia (Bold, Italic, Bold Italic);
   * Impact;
   * Times New Roman (Bold, Italic, Bold Italic);
   * Trebuchet (Bold, Italic, Bold Italic);
   * Verdana (Bold, Italic, Bold Italic);
   * Webdings.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
install -m 755 -d %{buildroot}/%{_datadir}/fonts/%{name}
cp -pr *.ttf %{buildroot}/%{_datadir}/fonts/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%dir %{_datadir}/fonts/%{name}
%{_datadir}/fonts/%{name}/*.ttf

%changelog
* Sun Aug  8 2010 Henrique (LonelySpooky) Junior <henriquecsj@gmail.com> - 1.0-1
- Initial package
