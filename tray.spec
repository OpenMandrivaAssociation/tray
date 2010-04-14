%define version 0.1
%define snapshot 20100413
%define rel 2
%define release %mkrel 0.%{snapshot}.%{rel}

Name:		tray
Version:	%{version}
Release:	%{release}
Summary:	Small tray applications and a volume daemon
License:	GPL
Group:		System/Base
URL:		http://git.mandriva.com/?p=projects/tray.git
# git archive --prefix=tray/ master | gzip > tray-$(date +%Y%m%d).tgz
Source0: 	tray-%{snapshot}.tgz
Patch0:		tray-20100413-reboot-tray-icon.diff
BuildRequires:	gtk+2-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	hal-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A collection of small GTK+ tray helpers and a volume daemon.

%prep
%setup -q -n tray
%patch0 -p1

%build
make
make locale

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
make install DESTDIR=%{buildroot}
install buttons.conf %{buildroot}%{_sysconfdir}/

%find_lang tray_keyleds
%find_lang tray_reboot
%find_lang tray_mixer
%find_lang tray_eject
%find_lang tray_randr
%find_lang tray_buttons

# ---------------------------------#

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

# ---------------------------------#

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

# ---------------------------------#

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

# ---------------------------------#

%package eject
Group: System/Base
Summary: Lightweight usb safe umount app

%description eject
tray_eject is lightweigth system tray app to safely umount usb storage devices.

%files eject -f tray_eject.lang
%defattr(0755,root,root,0755)
%{_bindir}/tray_eject
%defattr(0644,root,root,0755)
%{_datadir}/icons/tray_eject/*

# ---------------------------------#

%package randr
Group: System/Base
Summary: Lightweight randr app

%description randr
tray_randr is a lightweight system tray randr app.

%files randr -f tray_randr.lang
%defattr(0755,root,root,0755)
%{_bindir}/tray_randr
%defattr(0644,root,root,0755)
%{_datadir}/icons/tray_randr/*

# ---------------------------------#

%package buttons
Group: System/Base
Summary: Silly panel application that executes arbitray commands

%description buttons
tray_buttons is a silly panel application that executes arbitray commands
when these (configurable) buttons are pressed.

%files buttons -f tray_buttons.lang
%defattr(0755,root,root,0755)
%{_bindir}/tray_buttons
%defattr(0644,root,root,0755)
%{_datadir}/icons/tray_buttons/*
%{_sysconfdir}/buttons.conf

# ---------------------------------#

%package -n vold
Group: System/Base
Summary: Lighweight volume daemon

%description -n vold
vold is lightweigth daemon that listen for the volume multimedia keys (raise,
lower and mute) for light desktop environments.

%files -n vold
%defattr(0755,root,root,0755)
%{_bindir}/vold
%defattr(0644,root,root,0755)
%{_datadir}/icons/vold/*
