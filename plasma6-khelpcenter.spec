#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e 's,/,-,g')

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name: plasma6-khelpcenter
Version:	24.05.1
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/khelpcenter/-/archive/%{gitbranch}/khelpcenter-%{gitbranchd}.tar.bz2
%else
# was part of plasma but moved to applications in 16.04
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/khelpcenter-%{version}.tar.xz
%endif
Summary: KDE Plasma 6 Help Center
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: pkgconfig(xapian-core)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6XmlGui)

%description
KDE Plasma 6 Help Center.

%prep
%autosetup -p1 -n khelpcenter-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang khelpcenter --with-html --all-name || touch khelpcenter.lang

%files -f khelpcenter.lang
%{_datadir}/qlogging-categories6/khelpcenter.categories
%{_bindir}/khelpcenter
%{_libdir}/libexec/*
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.khelpcenter.desktop
%{_datadir}/dbus-1/services/org.kde.khelpcenter.service
%{_datadir}/config.kcfg/khelpcenter.kcfg
%{_datadir}/khelpcenter
