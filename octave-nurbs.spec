%define octpkg nurbs

Summary:	Routines for the creation, and manipulation of NURBS with Octave
Name:		octave-%{octpkg}
Version:	1.4.3
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/

BuildRequires:	octave-devel >= 5.1

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Collection of routines for the creation, and manipulation of Non-Uniform
Rational B-Splines (NURBS) with Octave, based on the NURBS toolbox by Mark
Spink.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

