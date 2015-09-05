#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

%define rel 1

Summary:        Libraries and daemons to implement searching in Akonadi
Name:           akonadi-search
Version: 15.08.0
Release:        %mkrel %rel
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)

BuildRequires:  kf5-macros
BuildRequires:  ki18n-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcrash-devel
BuildRequires:  akonadi-devel
BuildRequires:  kdepimlibs-devel
BuildRequires:  kmime-devel
BuildRequires:  kcalcore-devel

BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  xapian-devel

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
Libraries and daemons to implement searching in Akonadi

%files
%_kf5_bindir/akonadi_indexing_agent
%_qt5_plugindir/akonadi/*.so
%_sysconfdir/xdg/akonadi-search.categories
%_kf5_datadir/akonadi/agents/akonadiindexingagent.desktop

#--------------------------------------------------------------------

%define kf5akonadisearchcore_major 5
%define libkf5akonadisearchcore %mklibname kf5akonadisearchcore %{kf5akonadisearchcore_major}

%package -n %libkf5akonadisearchcore
Summary:      Libraries and daemons to implement searching in Akonadi
Group:        System/Libraries


%description -n %libkf5akonadisearchcore
Libraries and daemons to implement searching in Akonadi

%files -n %libkf5akonadisearchcore
%_kf5_libdir/libKF5AkonadiSearchCore.so.%{kf5akonadisearchcore_major}*

#--------------------------------------------------------------------

%define kf5akonadisearchpim_major 5
%define libkf5akonadisearchpim %mklibname kf5akonadisearchpim %{kf5akonadisearchpim_major}

%package -n %libkf5akonadisearchpim
Summary:      Akonadi Calendar Integration
Group:        System/Libraries


%description -n %libkf5akonadisearchpim
Akonadi Calendar Integration

%files -n %libkf5akonadisearchpim
%_kf5_libdir/libKF5AkonadiSearchPIM.so.%{kf5akonadisearchpim_major}*

#--------------------------------------------------------------------

%define kf5akonadisearchxapian_major 5
%define libkf5akonadisearchxapian %mklibname kf5akonadisearchxapian %{kf5akonadisearchxapian_major}

%package -n %libkf5akonadisearchxapian
Summary:      Akonadi Calendar Integration
Group:        System/Libraries


%description -n %libkf5akonadisearchxapian
Akonadi Calendar Integration

%files -n %libkf5akonadisearchxapian
%_kf5_libdir/libKF5AkonadiSearchXapian.so.%{kf5akonadisearchxapian_major}*

#--------------------------------------------------------------------

%define kf5akonadisearchcore_devel %mklibname kf5akonadisearch -d

%package -n %kf5akonadisearchcore_devel

Summary:        Devel stuff for %name
Group:          Development/KDE and Qt
Requires:       %libkf5akonadisearchcore = %version-%release
Requires:       %libkf5akonadisearchpim = %version-%release
Requires:       %libkf5akonadisearchxapian = %version-%release
Provides:       %name-devel = %{version}-%{release}

%description -n %kf5akonadisearchcore_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %kf5akonadisearchcore_devel
%_kf5_includedir/AkonadiSearch
%_kf5_includedir/*_version.h
%_kf5_libdir/*.so
%_kf5_libdir/cmake/KF5AkonadiSearch

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kf5
%make

%install
%makeinstall_std -C build

%find_lang --all %{name}5



%changelog
* Wed Aug 19 2015 neoclust <neoclust> 15.08.0-1.mga6
+ Revision: 865897
- New version 15.08.0

* Wed Aug 12 2015 neoclust <neoclust> 15.07.90-2.mga6
+ Revision: 863971
- Plasma Mass Rebuild - Rebuild for new Plasma

* Sun Aug 09 2015 neoclust <neoclust> 15.07.90-1.mga6
+ Revision: 861710
- New version 15.07.90

* Wed Jul 29 2015 neoclust <neoclust> 15.07.80-1.mga6
+ Revision: 858860
- imported package akonadi-search

