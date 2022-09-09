OPENQASM 2.0;
include "qelib1.inc";
qreg q[6];
creg c[3];

x q[1];
x q[2];
x q[4];
x q[5];
cx q[0], q[3];
x q[3];
cx q[1], q[4];
x q[4];
cx q[2], q[5];
x q[5];
measure q[3] -> c[3];
measure q[4] -> c[4];
measure q[5] -> c[5];
