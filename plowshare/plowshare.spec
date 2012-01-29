%global date 20120115

Name:           plowshare
Version:        0.9.4
Release:        0.25.%{date}git%{?dist}
Summary:        Download and upload files from file-sharing websites
Summary(pt_BR): Baixe e carregue arquivos em sites de compartilhamento
Summary(ru):    терминальный аплоадер/доунлоадер для наиболее популярных файлообменников
Group:          Applications/Internet
License:        GPLv3+
URL:            http://plowshare.googlecode.com
Source0:        http://plowshare.googlecode.com/files/%{name}-snapshot-git%{date}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  curl
Requires:  caca-utils
Requires:  recode
Requires:  ImageMagick
Requires:  js
%if 0%{?fedora}
Requires:  tesseract
%endif

BuildArch: noarch

%description
plowshare is a command-line downloader/uploader for some of the most popular
file-sharing websites. It works on UNIX-like systems and presently supports
Megaupload, Rapidshare, 2Shared, 4Shared, ZShare, Badongo, Depositfiles,
Mediafire, Netload.in, Storage.to, Uploaded.to, Uploading.com, Sendspace,
Usershare, X7.to and others.

%description -l pt_BR
plowshare é um cliente em linha de comando para baixar/carregar arquivos nos
mais populares sites de compartilhamento. Funciona em sistemas Unix-like e
atualmente suporta o Megaupload, RapidShare, 2Shared, 4Shared, Zshare, Badongo,
Depositfiles, Mediafire, Netload.in, Storage.to, Uploaded.to, Uploading.com,
Sendspace, Usershare, X7.to e outros.

%description -l ru
plowshare это терминальный аплоадер/доунлоадер для наиболее популярных файло-
обменников. Он работает на большинстве UNIX-подобных систем. На данный момент
поддерживаются следующие сервисы: Megaupload, Rapidshare, 2Shared, 4Shared,
ZShare, Badongo, DepositFiles и Mediafire. Смотрите README для подробностей.

%prep
%setup -q -n %{name}-snapshot-git%{date}

%build
# Nothing to build, it's simple bash scripts

%install
rm -rf %{buildroot}

DESTDIR=%{buildroot}  \
PREFIX=%{_prefix}     \
bash setup.sh install

# Programmable completion
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -p -m0644  etc/%{name}.completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}
sed -i 's|/local||g' \
    %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

# We remove at destination, so we still have install
# for the doc section
rm -rf %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING CHANGELOG
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_sysconfdir}/bash_completion.d/
%{_mandir}/man1/*
%{_mandir}/man5/%{name}.conf.5.*

%changelog
* Mon Jan 15 2012 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.25.20120115git
- New upstream snapshot

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.24.20111230git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 30 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.23.20111230git
- New upstream snapshot

* Tue Dec 06 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.22.20111206git
- New upstream snapshot

* Wed Nov 23 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.21.20111117git
- New upstream snapshot

* Tue Nov 15 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.20.20111114git
- New upstream snapshot

* Thu Nov 10 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.19.20111030git
- Update to new upstream snapshot

* Thu Oct 27 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.18.20111023git
- Update to new upstream snapshot

* Fri Oct 07 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.17.20110926git
- Update to new upstream snapshot
- Fixed CDIR path in programmable completion file

* Sun Sep 25 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.16.20110918git
- Update to new upstream snapshot
- File plowshare.completion renamed to plowshare

* Thu Sep 15 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.15.20110914git
- New upstream snapshot

* Tue Sep 06 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.14.20110904git
- New upstream snapshot

* Mon Aug 29 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.13.20110828git
- New upstream snapshot

* Wed Aug 17 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.12.20110816git
- Update to new upstream snapshot
- Add Brazilian Portuguese Translation (summary and description)
- New file from upstream: plowshare.completion
- Upstream is now using git instead of svn

* Tue Aug  9 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.11.svn1657
- Update to new upstream snapshot
- New manpage from upstream: plowshare.conf.5
- Another cosmetic change in spec file

* Sun Jul 31 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.10.svn1645
- New upstream snapshot
- File AUTHORS is now UTF-8

* Mon Jul 25 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.9.svn1630
- Update to new upstream snapshot
- New documentation file from upstream: AUTHORS
- Using iconv to convert character encoding for file AUTHORS from iso8859-1
  to utf-8.

* Sun Jul 17 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.8.svn1591
- Update to new upstream revision
- Removed dependency perl(Image::Magick). It's not necessary.

* Tue Jul 12 2011 Elder Marco <eldermarco@fedoraproject.org> - 0.9.4-0.7.svn1575
- Update to new upstream revision
- Cosmetics changes in spec file

* Sun Apr 24 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.6.svn1414
- Update to svn revision 1414 by request of Elder Marco by mail.

* Wed Mar 23 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.5.svn1394
- Update to new upstream revision (last befor import into Fedora).

* Mon Feb 28 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.4.svn1358
- Remove R gocr.

* Sun Feb 27 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.3.svn1358
- Delete bash from dependencies as it is common (thanks to Elder Marco).
- Fix summary.

* Sat Feb 26 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.2.svn1358
- Add BR perl(Image::Magick) and caca-utils (thanks to Elder Marco).

* Wed Feb 23 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.4-0.1.svn1358
- Update to last version.
- Adopt to upstream svn snapshots.
- Delete examples.
- lib.sh renamed to core.sh

* Tue Oct 5 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.3-2
- New version 0.9.3.
- Remove part %%{_prefix} from DESTDIR var and move it in new PREFIX one for
  script setup.sh
- Add files:
    o %%{_bindir}/plowlist and %%{_datadir}/%%{name}/list.sh
    o %%{_datadir}/%%{name}/tesseract
    o %%{_datadir}/%%{name}/strip_single_color.pl
    o %%{_datadir}/%%{name}/strip_threshold.pl
- Do not list all modules separately instead own full directory
  %%{_datadir}/%%{name}/modules/
- Add require gocr.
- Include mans: %%{_mandir}/man1/plow*.1*
- Include examples dir into %%doc and delete it from path where it installed
  automatically.

* Fri Nov 20 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.8.1-1
- Initial packaging.
- Optional requires aaview is not in Fedora repos. FR to support cacview
  filled:
  http://code.google.com/p/plowshare/issues/list?thanks=58&ts=1258746820
