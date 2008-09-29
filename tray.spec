%define version 0.1
%define snapshot 20080930
%define rel 1
%define release %mkrel 0.%{snapshot}.%{rel}

Name:		tray
Version:	%{version}
Release:	%{release}
Summary:	Small tray applications
License:	GPL
Group:		System/Base
URL:		http://helllabs.org/git/tray.git
# git archive --prefix=tray/ master | gzip > tray-$(date +%Y%m%d).tgz
Source0: 	tray-%{snapshot}.tgz
BuildRequires:	gtk+2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A collection of small GTK+ tray helpers.

%prep
%setup -q -n tray

%build
make
make locale

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
make install DESTDIR=%{buildroot}

%find_lang tray_keyleds
%find_lang tray_reboot
%find_lang tray_mixer

%package reboot
Group: System/Base
Summary: Shutdown/reboot helper for netbooks running finit

%description reboot
tray_reboot is a system tray helper to shutdown or reboot systems running
light desktop environments started by finit.

%files reboot -f tray_reboot.lang
%defattr(0755,root,root,0755)
%{_bindir}/tray_reboot
%defattr(0644,root,root,0755)
%{_datadir}/icons/tray_reboot/*

%package keyleds
Group: System/Base
Summary: Keyboard status helper for netbooks without physical LEDs

%description keyleds
tray_reboot is a {caps/num/scroll}lock status applet for 
light desktop environments started by finit.

%files keyleds -f tray_keyleds.lang
%defattr(0755,root,root,0755)
%{_bindir}/tray_keyleds
%defattr(0644,root,root,0755)
%{_datadir}/icons/tray_keyleds/*

%package mixer
Group: System/Base
Summary: Lightweight mixer 

%description mixer 
tray_mixer is lightweigth system tray mixer for light desktops environments 
started by finit.

%files mixer -f tray_mixer.lang
%defattr(0755,root,root,0755)
%{_bindir}/tray_mixer
%defattr(0644,root,root,0755)
%{_datadir}/icons/tray_mixer/*
