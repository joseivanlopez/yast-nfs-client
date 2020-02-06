#
# spec file for package yast2-nfs-client
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-nfs-client
Version:        4.1.8
Release:        0
Url:            https://github.com/yast/yast-nfs-client

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 3.1.27
BuildRequires:  yast2-testsuite
# Yast::Execute.locally
BuildRequires:  yast2 >= 4.1.42
BuildRequires:  rubygem(rspec)
#for install task
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# path_matching (RSpec argument matcher)
BuildRequires:  yast2-ruby-bindings >= 3.1.31
# Yast::Execute.locally
BuildRequires:  yast2 >= 4.1.42
#idmapd_conf agent
Requires:       yast2-nfs-common >= 2.24.0
# showmount, #150382, #286300
Recommends:     nfs-client
# Y2Storage::Filesystems::LegacyNfs#configure_from
Requires:       yast2-storage-ng >= 4.1.91
# Y2Storage::Filesystems::LegacyNfs#configure_from
BuildRequires:  yast2-storage-ng >= 4.1.91

# Unfortunately we cannot move this to macros.yast,
# bcond within macros are ignored by osc/OBS.
%bcond_with yast_run_ci_tests
%if %{with yast_run_ci_tests}
BuildRequires: rubygem(yast-rake-ci)
%endif

Provides:       yast2-config-nfs
Provides:       yast2-config-nfs-devel
Obsoletes:      yast2-config-nfs
Obsoletes:      yast2-config-nfs-devel
Provides:       yast2-trans-nfs
Obsoletes:      yast2-trans-nfs
Provides:       yast2-config-network:/usr/lib/YaST2/clients/lan_nfs_client.ycp

BuildArch:      noarch

Requires:       yast2-ruby-bindings >= 1.0.0

Summary:        YaST2 - NFS Configuration
License:        GPL-2.0-or-later
Group:          System/YaST

%description
The YaST2 component for configuration of NFS. NFS stands for network
file system access. It allows access to files on remote machines.

%prep
%setup -n %{name}-%{version}

%build

%check
rake test:unit

%install
rake install DESTDIR="%{buildroot}"

%files
%defattr(-,root,root)
%dir %{yast_yncludedir}/nfs
%{yast_yncludedir}/nfs/*
%dir %{yast_clientdir}
%{yast_clientdir}/nfs.rb
%{yast_clientdir}/nfs-client.rb
%{yast_clientdir}/nfs_auto.rb
%{yast_clientdir}/nfs-client4part.rb
%dir %{yast_moduledir}
%{yast_moduledir}/Nfs.rb
%{yast_moduledir}/NfsOptions.rb
%{yast_dir}/lib/y2nfs_client
%dir %{yast_desktopdir}
%{yast_desktopdir}/nfs.desktop
%{yast_icondir}
%doc %{yast_docdir}
%{yast_schemadir}/autoyast/rnc/nfs.rnc
%license COPYING

%changelog
