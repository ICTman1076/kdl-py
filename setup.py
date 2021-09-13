from setuptools import setup
import os.path, sys, tatsu, distutils, setuptools.command.build_py

here = os.path.dirname(os.path.abspath(__file__))

README = open(os.path.join(here, 'README.md'), 'rb').read()
README = README.decode()


class TatsuCommand(distutils.cmd.Command):
	"""Compile with Tatsu."""

	description = "Compile with Tatsu"
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		"""Run command."""
		here = os.getcwd()
		fromf = str(os.path.join(here, "kdl", "grammar.tatsu"))
		to = str(os.path.join(here, "kdl", "grammar.py"))
		self.announce("Buildin' from " + str(fromf), level=distutils.log.INFO)
		with open(fromf, "r") as f:
			code = str(tatsu.to_python_sourcecode(f.read(), name="Kdl"))
		self.announce("Writin' to " + to, level=distutils.log.INFO)
		with open(to, "w") as f:
			f.write(code)


class BuildPyCommand(setuptools.command.build_py.build_py):
	"""Custom build command."""

	def run(self):
		self.run_command("tatsu")
		setuptools.command.build_py.build_py.run(self)


# This call to setup() does all the work
setup(
	name="kdl-py",
	version="0.1.5",
	description="A Python library for the KDL Document Language.",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/daeken/kdl-py",
	author="Sera Brocious",
	author_email="sera.brocious@gmail.com",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3"
	],
	packages=["kdl"],
	include_package_data=True,
	install_requires=["TatSu >= 4.4.0", "regex >= 2021.4.4"],
	cmdclass={
		"tatsu": TatsuCommand,
		"build_py": BuildPyCommand
	},
)
