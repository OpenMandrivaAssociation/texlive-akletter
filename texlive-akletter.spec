# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/akletter
# catalog-date 2009-01-23 15:11:09 +0100
# catalog-license lppl
# catalog-version 1.5i
Name:		texlive-akletter
Version:	1.5i
Release:	11
Summary:	Comprehensive letter support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/akletter
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/akletter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/akletter.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An advanced letter document class which extends LaTeX's usual
letter class, providing support for building your own
letterhead and marking fold points for window envelopes.
Options supported by the package include: letterpaper for US
letter; a4offset for a modified A4 layout suitable for platic
binders that cover a part of the left margin. The class's
handling of dates has inspired an extended version of date-
handling in the isodate package. The class supersedes an
earlier class called myletter.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/akletter/akfax.cfg
%{_texmfdistdir}/tex/latex/akletter/akletter.cfg
%{_texmfdistdir}/tex/latex/akletter/akletter.cls
%{_texmfdistdir}/tex/latex/akletter/myletter.cls
%doc %{_texmfdistdir}/doc/latex/akletter/akletter.tex
%doc %{_texmfdistdir}/doc/latex/akletter/akletter.upl
%doc %{_texmfdistdir}/doc/latex/akletter/letterdoc.pdf
%doc %{_texmfdistdir}/doc/latex/akletter/letterdoc.tex
%doc %{_texmfdistdir}/doc/latex/akletter/lettereng.pdf
%doc %{_texmfdistdir}/doc/latex/akletter/lettereng.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
