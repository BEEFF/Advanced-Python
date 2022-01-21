# Multiprocessing

I first found out I needed to use multiprocessing when trying to execute a function with a maximum time limit. 

Multiprocessing is a package that supports spawning processes using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.

## Global Interpreter Lock
The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time. Locking the entire interpreter makes it easier for the interpreter to be multi-threaded, at the expense of much of the parallelism afforded by multi-processor machines.

