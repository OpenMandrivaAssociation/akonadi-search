%define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6AkonadiSearchCore
%define libKF6AkonadiSearchPIM %mklibname KPim6AkonadiSearchPIM
%define libKF6AkonadiSearchXapian %mklibname KPim6AkonadiSearchXapian
%define libKF6AkonadiSearchDebug %mklibname KPim6AkonadiSearchDebug
%define develname %mklibname KPim6AkonadiSearchCore -d

Summary:	Libraries and daemons to implement searching in Akonadi
Name:		plasma6-akonadi-search
Version:	24.01.96
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/akonadi-search/-/archive/%{gitbranch}/akonadi-search-%{gitbranchd}.tar.bz2#/akonadi-search-20240217.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/akonadi-search-%{version}.tar.xz
%endif
URL:		https://www.kde.org/
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Runner)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6TextUtils)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	xapian-devel
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
Requires:	%{libname} = %{EVRD}
Requires:	%{libKF6AkonadiSearchPIM} = %{EVRD}
Requires:	%{libKF6AkonadiSearchXapian} = %{EVRD}
Requires:	%{libKF6AkonadiSearchDebug} = %{EVRD}

%description
Libraries and daemons to implement searching in Akonadi.

%files -f akonadi_search.lang
%{_bindir}/akonadi_html_to_text
%{_bindir}/akonadi_indexing_agent
%{_datadir}/qlogging-categories6/akonadi-search.categories
%{_datadir}/qlogging-categories6/akonadi-search.renamecategories
%{_datadir}/akonadi/agents/akonadiindexingagent.desktop
%{_qtdir}/plugins/kf6/krunner/krunner_pimcontacts.so
%{_libdir}/qt6/plugins/kf6/krunner/kcms/kcm_krunner_pimcontacts.so
%{_libdir}/qt6/plugins/pim6/akonadi/*.so

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Akonadi search library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Obsoletes:	%{mklibname kf6akonadisearchcore 6} < 16.08.3
Conflicts:	%{mklibname kf6akonadisearchcore 6} < 16.08.3

%description -n %{libname}
Akonadi search library.

%files -n %{libname}
%{_libdir}/libKPim6AkonadiSearchCore.so*

#--------------------------------------------------------------------

%package -n %{libKF6AkonadiSearchPIM}
Summary:	Akonadi search library
Group:		System/Libraries
Obsoletes:	%{mklibname kf6akonadisearchpim 6} < 16.08.3
Conflicts:	%{mklibname kf6akonadisearchpim 6} < 16.08.3

%description -n %{libKF6AkonadiSearchPIM}
Akonadi search library.

%files -n %{libKF6AkonadiSearchPIM}
%{_libdir}/libKPim6AkonadiSearchPIM.so*

#--------------------------------------------------------------------

%package -n %{libKF6AkonadiSearchXapian}
Summary:	Akonadi search library
Group:		System/Libraries
Obsoletes:	%{mklibname kf6akonadisearchxapian 6} < 16.08.3
Conflicts:	%{mklibname kf6akonadisearchxapian 6} < 16.08.3

%description -n %{libKF6AkonadiSearchXapian}
Akonadi search library.

%files -n %{libKF6AkonadiSearchXapian}
%{_libdir}/libKPim6AkonadiSearchXapian.so*

#--------------------------------------------------------------------

%package -n %{libKF6AkonadiSearchDebug}
Summary:	Akonadi search library
Group:		System/Libraries
Obsoletes:	%{mklibname kf6akonadisearchdebug 6} < 16.08.3
Conflicts:	%{mklibname kf6akonadisearchdebug 6} < 16.08.3

%description -n %{libKF6AkonadiSearchDebug}
Akonadi search library.

%files -n %{libKF6AkonadiSearchDebug}
%{_libdir}/libKPim6AkonadiSearchDebug.so*

#--------------------------------------------------------------------

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:	%{mklibname KPim6AkonadiSearchCore} = %{EVRD}
Requires:	%{mklibname KPim6AkonadiSearchPIM} = %{EVRD}
Requires:	%{mklibname KPim6AkonadiSearchXapian} = %{EVRD}
Requires:	%{mklibname KPim6AkonadiSearchDebug} = %{EVRD}
Requires:	%{name} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}
Obsoletes:	%{mklibname kf6akonadisearch -d} < 16.08.2

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KPim6/AkonadiSearch
%{_libdir}/cmake/KPim6AkonadiSearch

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n akonadi-search-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang akonadi_search
