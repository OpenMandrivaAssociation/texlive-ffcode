%global tl_name ffcode
%global tl_revision 79167

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.12.1
Release:	%{tl_revision}.1
Summary:	Fixed-font code blocks formatted nicely
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ffcode
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ffcode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ffcode.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ffcode.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(listings)
Requires:	texlive(pgfopts)
Requires:	texlive(tcolorbox)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package helps you write source code in your academic papers
and make it looks neat. It uses listings and tcolorbox, configuring them
the right way, to ensure that code fragments and code blocks look nicer.

