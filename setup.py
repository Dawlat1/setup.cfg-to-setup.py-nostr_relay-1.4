from setuptools import setup, find_packages


description={'nostr relay'}

long_description = {'file': 'README.md'}

long_description_content_type = {"text/markdown"}

license = {"BSD 3-Clause License"}

classifiers = [
      "License :: OSI Approved :: BSD License",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Programming Language :: Python :: 3.11",
      "Programming Language :: Python :: 3.12",
      "Development Status :: 5 - Production/Stable",
      "Environment :: Web Environment",
      "Intended Audience :: System Administrators",
      "Operating System :: OS Independent",
      "Topic :: Internet :: WWW/HTTP",
] 

packages = find_packages(
      where='nostr_relay',
      include = ['nostr_relay.storage','nostr_relay.recipe'],      
)

package_data = \
{'': ['*']}

package_dir = \
{'nostr_relay.storage':'nostr_relay',
'nostr_relay.recipe':'nostr_relay'}

extras_require = {
      'test': ['pytest', 'pytest-cov','pytest-asyncio','pytest-xdist'],
      'postgres': ['asyncpg'],
      'lmdb': ['lmdb','msgpack','whoosh']
}

entry_points = \
{'console_scripts': ['nostr-relay = nostr_relay.cli:main']}

install_requires = [
      "falcon",
      #"python-rapidjson; platform_python_implementation=='CPython'",
      #"aionostr>=0.20.0",
      #"sqlalchemy[asyncio]>=2.0",
      #"aiosqlite>=0.20.0",
      #"aiohttp[speedups]",
      #"uvicorn[standard]",
      #"gunicorn",
	#"setproctitle",
      #"alembic",
      #"pydantic>2.0",
      #"async-timeout; python_version < '3.11.0'",
      "wsproto; platform_python_implementation!='CPython'",
]
egg_info= \
{'tag_build':['tag_date=0']}
	
setup(name='nostr_relay',
      version='1.4',
      description=description,
      long_description=long_description,
      long_description_content_type=long_description_content_type,
      author="Dave St.Germain",
      author_email='dave@st.germa.in',
      url='https://code.pobblelabs.org/nostr_relay',
      classifiers=classifiers,
      packages=packages,
      package_data=package_data,
      package_dir=package_dir,
      extras_require=extras_require,
      entry_points=entry_points,
      keywords=["protocol"],
      python_requires='>=3.8',
      #requires=requires,
      install_requires=install_requires,
      zip_safe = True,
      include_package_data = True,
      #setup_requires=["flake8"]
     )