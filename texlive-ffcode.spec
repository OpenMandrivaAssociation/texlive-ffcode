Name:		texlive-ffcode
Version:	65170
Release:	1
Summary:	Fixed-font code blocks formatted nicely
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ffcode
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ffcode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ffcode.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ffcode.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package helps you write source code in your academic
papers and make it looks neat. It uses minted and tcolorbox,
configuring them the right way, to ensure that code fragments
and code blocks look nicer.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ffcode
%{_texmfdistdir}/tex/latex/ffcode
%doc %{_texmfdistdir}/doc/latex/ffcode

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
