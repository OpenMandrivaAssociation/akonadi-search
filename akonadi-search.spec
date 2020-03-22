%define major 5
%define libname %mklibname KF5AkonadiSearchCore %{major}
%define libKF5AkonadiSearchPIM %mklibname KF5AkonadiSearchPIM %{major}
%define libKF5AkonadiSearchXapian %mklibname KF5AkonadiSearchXapian %{major}
%define libKF5AkonadiSearchDebug %mklibname KF5AkonadiSearchDebug %{major}
%define develname %mklibname KF5AkonadiSearchCore -d

Summary:	Libraries and daemons to implement searching in Akonadi
Name:		akonadi-search
Version:	20.03.80
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Runner)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	xapian-devel
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
Requires:	%{libname} = %{EVRD}
Requires:	%{libKF5AkonadiSearchPIM} = %{EVRD}
Requires:	%{libKF5AkonadiSearchXapian} = %{EVRD}
Requires:	%{libKF5AkonadiSearchDebug} = %{EVRD}

%description
Libraries and daemons to implement searching in Akonadi.

%files -f akonadi_search.lang
%{_bindir}/akonadi_indexing_agent
%{_qt5_plugindir}/akonadi/*.so
%{_qt5_plugindir}/*.so
%{_datadir}/qlogging-categories5/akonadi-search.categories
%{_datadir}/qlogging-categories5/akonadi-search.renamecategories
%{_datadir}/akonadi/agents/akonadiindexingagent.desktop
%{_datadir}/kservices5/*.desktop

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Akonadi search library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Obsoletes:	%{mklibname kf5akonadisearchcore 5} < 16.08.3
Conflicts:	%{mklibname kf5akonadisearchcore 5} < 16.08.3

%description -n %{libname}
Akonadi search library.

%files -n %{libname}
%{_libdir}/libKF5AkonadiSearchCore.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libKF5AkonadiSearchPIM}
Summary:	Akonadi search library
Group:		System/Libraries
Obsoletes:	%{mklibname kf5akonadisearchpim 5} < 16.08.3
Conflicts:	%{mklibname kf5akonadisearchpim 5} < 16.08.3

%description -n %{libKF5AkonadiSearchPIM}
Akonadi search library.

%files -n %{libKF5AkonadiSearchPIM}
%{_libdir}/libKF5AkonadiSearchPIM.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libKF5AkonadiSearchXapian}
Summary:	Akonadi search library
Group:		System/Libraries
Obsoletes:	%{mklibname kf5akonadisearchxapian 5} < 16.08.3
Conflicts:	%{mklibname kf5akonadisearchxapian 5} < 16.08.3

%description -n %{libKF5AkonadiSearchXapian}
Akonadi search library.

%files -n %{libKF5AkonadiSearchXapian}
%{_libdir}/libKF5AkonadiSearchXapian.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libKF5AkonadiSearchDebug}
Summary:	Akonadi search library
Group:		System/Libraries
Obsoletes:	%{mklibname kf5akonadisearchdebug 5} < 16.08.3
Conflicts:	%{mklibname kf5akonadisearchdebug 5} < 16.08.3

%description -n %{libKF5AkonadiSearchDebug}
Akonadi search library.

%files -n %{libKF5AkonadiSearchDebug}
%{_libdir}/libKF5AkonadiSearchDebug.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:	%{mklibname KF5AkonadiSearchCore %{major}} = %{EVRD}
Requires:	%{mklibname KF5AkonadiSearchPIM %{major}} = %{EVRD}
Requires:	%{mklibname KF5AkonadiSearchXapian %{major}} = %{EVRD}
Requires:	%{mklibname KF5AkonadiSearchDebug %{major}} = %{EVRD}
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
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang akonadi_search
