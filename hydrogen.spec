Summary:	Pattern based drum machine
Name:		hydrogen
Version:	0.9.6
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	https://github.com/hydrogen-music/hydrogen/archive/%{version}.tar.gz
# Source0-md5:	e4424926a88af82fb2048b3548723827
URL:		http://www.hydrogen-music.org/
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	flac-c++-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libarchive-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hydrogen is a "free" pattern based drum machine for GNU/Linux. The
application goal is to allow the simple and fast creation of rhythmic
patterns.

%package doc
Summary:	Hydrogen manual and tutorial
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Hydrogen manual and tutorial.

%prep
%setup -q

%build
mkdir build
cd build
%cmake .. \
	-DWANT_ALSA=1		\
	-DWANT_DEBUG=1		\
	-DWANT_JACK=1		\
	-DWANT_LRDF=1		\
	-DWANT_OSS=0		\
	-DWANT_PORTAUDIO=0	\
	-DWANT_PORTMIDI=0	\
	-DWANT_SHARED=0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# clean up
%{__rm} $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/*.docbook
%{__rm} $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/doc/img/*.h2song
%{__rm} $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/i18n/*.ts
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}

install data/doc/img/Tutorial2.h2song \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/demo_songs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DEVELOPERS INSTALL.txt README.txt
# don't package h2synth, just a test
%attr(755,root,root) %{_bindir}/h2cli
%attr(755,root,root) %{_bindir}/h2player
%attr(755,root,root) %{_bindir}/hydrogen

%dir %{_datadir}/hydrogen
%dir %{_datadir}/hydrogen/data
%dir %{_datadir}/hydrogen/data/demo_songs
%dir %{_datadir}/hydrogen/data/i18n

%{_datadir}/hydrogen/data/*.conf
%{_datadir}/hydrogen/data/*.h2song
%{_datadir}/hydrogen/data/*.wav
%{_datadir}/hydrogen/data/drumkits
%{_datadir}/hydrogen/data/img
%{_datadir}/hydrogen/data/xsd

%{_desktopdir}/*.desktop
#%{_pixmapsdir}/*.png

# demo songs
%{_datadir}/hydrogen/data/demo_songs/GM_*.h2song
%{_datadir}/hydrogen/data/demo_songs/TR808kit-demo.h2song
%{_datadir}/hydrogen/data/demo_songs/Tutorial2.h2song
%{_datadir}/hydrogen/data/demo_songs/tutorial_georgyporgy.h2song

# translations
%lang(de) %{_datadir}/hydrogen/data/i18n/%{name}.de.qm
%lang(es) %{_datadir}/hydrogen/data/i18n/%{name}.es.qm
%lang(fr) %{_datadir}/hydrogen/data/i18n/%{name}.fr.qm
%lang(hu) %{_datadir}/hydrogen/data/i18n/%{name}.hu_HU.qm
%lang(it) %{_datadir}/hydrogen/data/i18n/%{name}.it.qm
%lang(ja) %{_datadir}/hydrogen/data/i18n/%{name}.ja.qm
%lang(nl) %{_datadir}/hydrogen/data/i18n/%{name}.nl.qm
%lang(pl) %{_datadir}/hydrogen/data/i18n/%{name}.pl.qm
%lang(pt) %{_datadir}/hydrogen/data/i18n/%{name}.pt_BR.qm
%lang(ru) %{_datadir}/hydrogen/data/i18n/%{name}.ru.qm

%files doc
%defattr(644,root,root,755)
%dir %{_datadir}/hydrogen/data/doc
%dir %{_datadir}/hydrogen/data/doc/img

# images
%lang(nl) %dir %{_datadir}/hydrogen/data/doc/img/nl
%lang(nl) %{_datadir}/hydrogen/data/doc/img/nl/*.png
%{_datadir}/hydrogen/data/doc/img/*.png
%{_datadir}/hydrogen/data/doc/img_tutorial
%{_datadir}/hydrogen/data/doc/infoSplash

%{_datadir}/hydrogen/data/doc/manual.html
%{_datadir}/hydrogen/data/new_tutorial


