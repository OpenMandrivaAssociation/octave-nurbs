%global octpkg nurbs

Summary:	Routines for the creation, and manipulation of NURBS with Octave
Name:		octave-nurbs
Version:	1.4.4
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/nurbs/
Source0:	https://downloads.sourceforge.net/octave/nurbs-%{version}.tar.gz

BuildRequires:  octave-devel >= 5.1.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Collection of routines for the creation, and manipulation of
Non-Uniform Rational B-Splines (NURBS), based on the NURBS toolbox.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

