Summary:	Libraries and daemons to implement searching in Akonadi
Name:		akonadi-search
Version:	16.08.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
URL:		https://www.kde.org/
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Runner)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	xapian-devel
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
Libraries and daemons to implement searching in Akonadi.

%files
%{_bindir}/akonadi_indexing_agent
%{_qt5_plugindir}/akonadi/*.so
%{_qt5_plugindir}/*.so
%{_sysconfdir}/xdg/akonadi-search.categories
%{_datadir}/akonadi/agents/akonadiindexingagent.desktop
%{_datadir}/kservices5/*.desktop

#--------------------------------------------------------------------

%libpackage KF5AkonadiSearchCore 5
%libpackage KF5AkonadiSearchPIM 5
%libpackage KF5AkonadiSearchXapian 5
%libpackage KF5AkonadiSearchDebug 5


%define develname %mklibname kf5akonadisearch -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:	%{mklibname KF5AkonadiSearchCore 5} = %{EVRD}
Requires:	%{mklibname KF5AkonadiSearchPIM 5} = %{EVRD}
Requires:	%{mklibname KF5AkonadiSearchXapian 5} = %{EVRD}
Requires:	%{mklibname KF5AkonadiSearchDebug 5} = %{EVRD}
Requires:	%{name} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}
Obsoletes:	%{mklibname kf5akonadisearch -d} < 16.08.2

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KF5/AkonadiSearch
%{_includedir}/KF5/*_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5AkonadiSearch

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
