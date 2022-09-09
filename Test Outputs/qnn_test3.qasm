OPENQASM 2.0;
include "qelib1.inc";
qreg q[43];
creg c[8];

x q[9];
x q[8];
x q[11];
x q[16];
x q[14];
x q[13];
h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];
ccx q[8], q[0], q[38];
ccx q[9], q[0], q[39];
cx q[40], q[38];
cx q[40], q[39];
cx q[40], q[18];
cx q[40], q[19];
cx q[40], q[20];
cx q[40], q[18];
cswap q[18], q[38], q[40];
cx q[40], q[19];
cswap q[19], q[39], q[40];
cx q[40], q[20];
cswap q[19], q[39], q[40];
cx q[39], q[19];
cswap q[18], q[38], q[40];
cx q[38], q[18];
cx q[40], q[20];
cx q[40], q[19];
cx q[40], q[18];
cx q[40], q[39];
cx q[40], q[38];
ccx q[9], q[0], q[39];
ccx q[8], q[0], q[38];
ccx q[8], q[1], q[38];
ccx q[9], q[1], q[39];
cx q[40], q[38];
cx q[40], q[39];
cx q[40], q[19];
cx q[40], q[20];
cx q[40], q[21];
cx q[40], q[19];
cswap q[19], q[38], q[40];
cx q[40], q[20];
cswap q[20], q[39], q[40];
cx q[40], q[21];
cswap q[20], q[39], q[40];
cx q[39], q[20];
cswap q[19], q[38], q[40];
cx q[38], q[19];
cx q[40], q[21];
cx q[40], q[20];
cx q[40], q[19];
cx q[40], q[39];
cx q[40], q[38];
ccx q[9], q[1], q[39];
ccx q[8], q[1], q[38];
ccx q[10], q[2], q[38];
ccx q[11], q[2], q[39];
cx q[40], q[38];
cx q[40], q[39];
cx q[40], q[22];
cx q[40], q[23];
cx q[40], q[24];
cx q[40], q[22];
cswap q[22], q[38], q[40];
cx q[40], q[23];
cswap q[23], q[39], q[40];
cx q[40], q[24];
cswap q[23], q[39], q[40];
cx q[39], q[23];
cswap q[22], q[38], q[40];
cx q[38], q[22];
cx q[40], q[24];
cx q[40], q[23];
cx q[40], q[22];
cx q[40], q[39];
cx q[40], q[38];
ccx q[11], q[2], q[39];
ccx q[10], q[2], q[38];
ccx q[10], q[3], q[38];
ccx q[11], q[3], q[39];
cx q[40], q[38];
cx q[40], q[39];
cx q[40], q[23];
cx q[40], q[24];
cx q[40], q[25];
cx q[40], q[23];
cswap q[23], q[38], q[40];
cx q[40], q[24];
cswap q[24], q[39], q[40];
cx q[40], q[25];
cswap q[24], q[39], q[40];
cx q[39], q[24];
cswap q[23], q[38], q[40];
cx q[38], q[23];
cx q[40], q[25];
cx q[40], q[24];
cx q[40], q[23];
cx q[40], q[39];
cx q[40], q[38];
ccx q[11], q[3], q[39];
ccx q[10], q[3], q[38];
ccx q[18], q[4], q[38];
ccx q[19], q[4], q[39];
ccx q[20], q[4], q[40];
ccx q[21], q[4], q[41];
cx q[42], q[38];
cx q[42], q[39];
cx q[42], q[40];
cx q[42], q[41];
cx q[42], q[26];
cx q[42], q[27];
cx q[42], q[28];
cx q[42], q[29];
cx q[42], q[30];
cx q[42], q[26];
cswap q[26], q[38], q[42];
cx q[42], q[27];
cswap q[27], q[39], q[42];
cx q[42], q[28];
cswap q[28], q[40], q[42];
cx q[42], q[29];
cswap q[29], q[41], q[42];
cx q[42], q[30];
cswap q[29], q[41], q[42];
cx q[41], q[29];
cswap q[28], q[40], q[42];
cx q[40], q[28];
cswap q[27], q[39], q[42];
cx q[39], q[27];
cswap q[26], q[38], q[42];
cx q[38], q[26];
cx q[42], q[30];
cx q[42], q[29];
cx q[42], q[28];
cx q[42], q[27];
cx q[42], q[26];
cx q[42], q[41];
cx q[42], q[40];
cx q[42], q[39];
cx q[42], q[38];
ccx q[21], q[4], q[41];
ccx q[20], q[4], q[40];
ccx q[19], q[4], q[39];
ccx q[18], q[4], q[38];
ccx q[18], q[5], q[38];
ccx q[19], q[5], q[39];
ccx q[20], q[5], q[40];
ccx q[21], q[5], q[41];
cx q[42], q[38];
cx q[42], q[39];
cx q[42], q[40];
cx q[42], q[41];
cx q[42], q[27];
cx q[42], q[28];
cx q[42], q[29];
cx q[42], q[30];
cx q[42], q[31];
cx q[42], q[27];
cswap q[27], q[38], q[42];
cx q[42], q[28];
cswap q[28], q[39], q[42];
cx q[42], q[29];
cswap q[29], q[40], q[42];
cx q[42], q[30];
cswap q[30], q[41], q[42];
cx q[42], q[31];
cswap q[30], q[41], q[42];
cx q[41], q[30];
cswap q[29], q[40], q[42];
cx q[40], q[29];
cswap q[28], q[39], q[42];
cx q[39], q[28];
cswap q[27], q[38], q[42];
cx q[38], q[27];
cx q[42], q[31];
cx q[42], q[30];
cx q[42], q[29];
cx q[42], q[28];
cx q[42], q[27];
cx q[42], q[41];
cx q[42], q[40];
cx q[42], q[39];
cx q[42], q[38];
ccx q[21], q[5], q[41];
ccx q[20], q[5], q[40];
ccx q[19], q[5], q[39];
ccx q[18], q[5], q[38];
ccx q[22], q[6], q[38];
ccx q[23], q[6], q[39];
ccx q[24], q[6], q[40];
ccx q[25], q[6], q[41];
cx q[42], q[38];
cx q[42], q[39];
cx q[42], q[40];
cx q[42], q[41];
cx q[42], q[32];
cx q[42], q[33];
cx q[42], q[34];
cx q[42], q[35];
cx q[42], q[36];
cx q[42], q[32];
cswap q[32], q[38], q[42];
cx q[42], q[33];
cswap q[33], q[39], q[42];
cx q[42], q[34];
cswap q[34], q[40], q[42];
cx q[42], q[35];
cswap q[35], q[41], q[42];
cx q[42], q[36];
cswap q[35], q[41], q[42];
cx q[41], q[35];
cswap q[34], q[40], q[42];
cx q[40], q[34];
cswap q[33], q[39], q[42];
cx q[39], q[33];
cswap q[32], q[38], q[42];
cx q[38], q[32];
cx q[42], q[36];
cx q[42], q[35];
cx q[42], q[34];
cx q[42], q[33];
cx q[42], q[32];
cx q[42], q[41];
cx q[42], q[40];
cx q[42], q[39];
cx q[42], q[38];
ccx q[25], q[6], q[41];
ccx q[24], q[6], q[40];
ccx q[23], q[6], q[39];
ccx q[22], q[6], q[38];
ccx q[22], q[7], q[38];
ccx q[23], q[7], q[39];
ccx q[24], q[7], q[40];
ccx q[25], q[7], q[41];
cx q[42], q[38];
cx q[42], q[39];
cx q[42], q[40];
cx q[42], q[41];
cx q[42], q[33];
cx q[42], q[34];
cx q[42], q[35];
cx q[42], q[36];
cx q[42], q[37];
cx q[42], q[33];
cswap q[33], q[38], q[42];
cx q[42], q[34];
cswap q[34], q[39], q[42];
cx q[42], q[35];
cswap q[35], q[40], q[42];
cx q[42], q[36];
cswap q[36], q[41], q[42];
cx q[42], q[37];
cswap q[36], q[41], q[42];
cx q[41], q[36];
cswap q[35], q[40], q[42];
cx q[40], q[35];
cswap q[34], q[39], q[42];
cx q[39], q[34];
cswap q[33], q[38], q[42];
cx q[38], q[33];
cx q[42], q[37];
cx q[42], q[36];
cx q[42], q[35];
cx q[42], q[34];
cx q[42], q[33];
cx q[42], q[41];
cx q[42], q[40];
cx q[42], q[39];
cx q[42], q[38];
ccx q[25], q[7], q[41];
ccx q[24], q[7], q[40];
ccx q[23], q[7], q[39];
ccx q[22], q[7], q[38];
cx q[37], q[32];
cx q[37], q[33];
cx q[37], q[34];
cx q[37], q[35];
cx q[37], q[36];
cx q[37], q[26];
cx q[37], q[27];
cx q[37], q[28];
cx q[37], q[29];
cx q[37], q[30];
cx q[37], q[31];
cx q[37], q[26];
cswap q[26], q[32], q[37];
cx q[37], q[27];
cswap q[27], q[33], q[37];
cx q[37], q[28];
cswap q[28], q[34], q[37];
cx q[37], q[29];
cswap q[29], q[35], q[37];
cx q[37], q[30];
cswap q[30], q[36], q[37];
cx q[37], q[31];
cswap q[30], q[36], q[37];
cx q[36], q[30];
cswap q[29], q[35], q[37];
cx q[35], q[29];
cswap q[28], q[34], q[37];
cx q[34], q[28];
cswap q[27], q[33], q[37];
cx q[33], q[27];
cswap q[26], q[32], q[37];
cx q[32], q[26];
cx q[37], q[31];
cx q[37], q[30];
cx q[37], q[29];
cx q[37], q[28];
cx q[37], q[27];
cx q[37], q[26];
cx q[37], q[36];
cx q[37], q[35];
cx q[37], q[34];
cx q[37], q[33];
cx q[37], q[32];
cx q[12], q[26];
x q[26];
cx q[13], q[27];
x q[27];
cx q[14], q[28];
x q[28];
cx q[15], q[29];
x q[29];
cx q[16], q[30];
x q[30];
cx q[17], q[31];
x q[31];
h q[38];
cp(-pi/4) q[26], q[38];
cx q[26], q[27];
cp(pi/4) q[27], q[38];
cx q[26], q[27];
cp(-pi/4) q[27], q[38];
cx q[27], q[28];
cp(pi/4) q[28], q[38];
cx q[26], q[28];
cp(-pi/4) q[28], q[38];
cx q[27], q[28];
cp(pi/4) q[28], q[38];
cx q[26], q[28];
cp(-pi/4) q[28], q[38];
h q[38];
h q[39];
cp(-pi/4) q[29], q[39];
cx q[29], q[30];
cp(pi/4) q[30], q[39];
cx q[29], q[30];
cp(-pi/4) q[30], q[39];
cx q[30], q[38];
cp(pi/4) q[38], q[39];
cx q[29], q[38];
cp(-pi/4) q[38], q[39];
cx q[30], q[38];
cp(pi/4) q[38], q[39];
cx q[29], q[38];
cp(-pi/4) q[38], q[39];
h q[39];
h q[40];
cp(-pi/4) q[31], q[40];
cx q[31], q[26];
cp(pi/4) q[26], q[40];
cx q[31], q[26];
cp(-pi/4) q[26], q[40];
cx q[26], q[39];
cp(pi/4) q[39], q[40];
cx q[31], q[39];
cp(-pi/4) q[39], q[40];
cx q[26], q[39];
cp(pi/4) q[39], q[40];
cx q[31], q[39];
cp(-pi/4) q[39], q[40];
h q[40];
h q[41];
cp(-pi/4) q[27], q[41];
cx q[27], q[28];
cp(pi/4) q[28], q[41];
cx q[27], q[28];
cp(-pi/4) q[28], q[41];
cx q[28], q[40];
cp(pi/4) q[40], q[41];
cx q[27], q[40];
cp(-pi/4) q[40], q[41];
cx q[28], q[40];
cp(pi/4) q[40], q[41];
cx q[27], q[40];
cp(-pi/4) q[40], q[41];
h q[41];
h q[42];
cp(-pi/4) q[29], q[42];
cx q[29], q[30];
cp(pi/4) q[30], q[42];
cx q[29], q[30];
cp(-pi/4) q[30], q[42];
cx q[30], q[41];
cp(pi/4) q[41], q[42];
cx q[29], q[41];
cp(-pi/4) q[41], q[42];
cx q[30], q[41];
cp(pi/4) q[41], q[42];
cx q[29], q[41];
cp(-pi/4) q[41], q[42];
h q[42];
cz q[42], q[31];
h q[42];
cp(-pi/4) q[41], q[42];
cx q[29], q[41];
cp(pi/4) q[41], q[42];
cx q[30], q[41];
cp(-pi/4) q[41], q[42];
cx q[29], q[41];
cp(pi/4) q[41], q[42];
cx q[30], q[41];
cp(-pi/4) q[30], q[42];
cx q[29], q[30];
cp(pi/4) q[30], q[42];
cx q[29], q[30];
cp(-pi/4) q[29], q[42];
h q[42];
h q[41];
cp(-pi/4) q[40], q[41];
cx q[27], q[40];
cp(pi/4) q[40], q[41];
cx q[28], q[40];
cp(-pi/4) q[40], q[41];
cx q[27], q[40];
cp(pi/4) q[40], q[41];
cx q[28], q[40];
cp(-pi/4) q[28], q[41];
cx q[27], q[28];
cp(pi/4) q[28], q[41];
cx q[27], q[28];
cp(-pi/4) q[27], q[41];
h q[41];
h q[40];
cp(-pi/4) q[39], q[40];
cx q[31], q[39];
cp(pi/4) q[39], q[40];
cx q[26], q[39];
cp(-pi/4) q[39], q[40];
cx q[31], q[39];
cp(pi/4) q[39], q[40];
cx q[26], q[39];
cp(-pi/4) q[26], q[40];
cx q[31], q[26];
cp(pi/4) q[26], q[40];
cx q[31], q[26];
cp(-pi/4) q[31], q[40];
h q[40];
h q[39];
cp(-pi/4) q[38], q[39];
cx q[29], q[38];
cp(pi/4) q[38], q[39];
cx q[30], q[38];
cp(-pi/4) q[38], q[39];
cx q[29], q[38];
cp(pi/4) q[38], q[39];
cx q[30], q[38];
cp(-pi/4) q[30], q[39];
cx q[29], q[30];
cp(pi/4) q[30], q[39];
cx q[29], q[30];
cp(-pi/4) q[29], q[39];
h q[39];
h q[38];
cp(-pi/4) q[28], q[38];
cx q[26], q[28];
cp(pi/4) q[28], q[38];
cx q[27], q[28];
cp(-pi/4) q[28], q[38];
cx q[26], q[28];
cp(pi/4) q[28], q[38];
cx q[27], q[28];
cp(-pi/4) q[27], q[38];
cx q[26], q[27];
cp(pi/4) q[27], q[38];
cx q[26], q[27];
cp(-pi/4) q[26], q[38];
h q[38];
x q[31];
cx q[17], q[31];
x q[30];
cx q[16], q[30];
x q[29];
cx q[15], q[29];
x q[28];
cx q[14], q[28];
x q[27];
cx q[13], q[27];
x q[26];
cx q[12], q[26];
cx q[37], q[32];
cx q[37], q[33];
cx q[37], q[34];
cx q[37], q[35];
cx q[37], q[36];
cx q[37], q[26];
cx q[37], q[27];
cx q[37], q[28];
cx q[37], q[29];
cx q[37], q[30];
cx q[37], q[31];
cx q[32], q[26];
cswap q[26], q[32], q[37];
cx q[33], q[27];
cswap q[27], q[33], q[37];
cx q[34], q[28];
cswap q[28], q[34], q[37];
cx q[35], q[29];
cswap q[29], q[35], q[37];
cx q[36], q[30];
cswap q[30], q[36], q[37];
cx q[37], q[31];
cswap q[30], q[36], q[37];
cx q[37], q[30];
cswap q[29], q[35], q[37];
cx q[37], q[29];
cswap q[28], q[34], q[37];
cx q[37], q[28];
cswap q[27], q[33], q[37];
cx q[37], q[27];
cswap q[26], q[32], q[37];
cx q[37], q[26];
cx q[37], q[31];
cx q[37], q[30];
cx q[37], q[29];
cx q[37], q[28];
cx q[37], q[27];
cx q[37], q[26];
cx q[37], q[36];
cx q[37], q[35];
cx q[37], q[34];
cx q[37], q[33];
cx q[37], q[32];
ccx q[22], q[7], q[38];
ccx q[23], q[7], q[39];
ccx q[24], q[7], q[40];
ccx q[25], q[7], q[41];
cx q[42], q[38];
cx q[42], q[39];
cx q[42], q[40];
cx q[42], q[41];
cx q[42], q[33];
cx q[42], q[34];
cx q[42], q[35];
cx q[42], q[36];
cx q[42], q[37];
cx q[38], q[33];
cswap q[33], q[38], q[42];
cx q[39], q[34];
cswap q[34], q[39], q[42];
cx q[40], q[35];
cswap q[35], q[40], q[42];
cx q[41], q[36];
cswap q[36], q[41], q[42];
cx q[42], q[37];
cswap q[36], q[41], q[42];
cx q[42], q[36];
cswap q[35], q[40], q[42];
cx q[42], q[35];
cswap q[34], q[39], q[42];
cx q[42], q[34];
cswap q[33], q[38], q[42];
cx q[42], q[33];
cx q[42], q[37];
cx q[42], q[36];
cx q[42], q[35];
cx q[42], q[34];
cx q[42], q[33];
cx q[42], q[41];
cx q[42], q[40];
cx q[42], q[39];
cx q[42], q[38];
ccx q[25], q[7], q[41];
ccx q[24], q[7], q[40];
ccx q[23], q[7], q[39];
ccx q[22], q[7], q[38];
ccx q[22], q[6], q[38];
ccx q[23], q[6], q[39];
ccx q[24], q[6], q[40];
ccx q[25], q[6], q[41];
cx q[42], q[38];
cx q[42], q[39];
cx q[42], q[40];
cx q[42], q[41];
cx q[42], q[32];
cx q[42], q[33];
cx q[42], q[34];
cx q[42], q[35];
cx q[42], q[36];
cx q[38], q[32];
cswap q[32], q[38], q[42];
cx q[39], q[33];
cswap q[33], q[39], q[42];
cx q[40], q[34];
cswap q[34], q[40], q[42];
cx q[41], q[35];
cswap q[35], q[41], q[42];
cx q[42], q[36];
cswap q[35], q[41], q[42];
cx q[42], q[35];
cswap q[34], q[40], q[42];
cx q[42], q[34];
cswap q[33], q[39], q[42];
cx q[42], q[33];
cswap q[32], q[38], q[42];
cx q[42], q[32];
cx q[42], q[36];
cx q[42], q[35];
cx q[42], q[34];
cx q[42], q[33];
cx q[42], q[32];
cx q[42], q[41];
cx q[42], q[40];
cx q[42], q[39];
cx q[42], q[38];
ccx q[25], q[6], q[41];
ccx q[24], q[6], q[40];
ccx q[23], q[6], q[39];
ccx q[22], q[6], q[38];
ccx q[18], q[5], q[38];
ccx q[19], q[5], q[39];
ccx q[20], q[5], q[40];
ccx q[21], q[5], q[41];
cx q[42], q[38];
cx q[42], q[39];
cx q[42], q[40];
cx q[42], q[41];
cx q[42], q[27];
cx q[42], q[28];
cx q[42], q[29];
cx q[42], q[30];
cx q[42], q[31];
cx q[38], q[27];
cswap q[27], q[38], q[42];
cx q[39], q[28];
cswap q[28], q[39], q[42];
cx q[40], q[29];
cswap q[29], q[40], q[42];
cx q[41], q[30];
cswap q[30], q[41], q[42];
cx q[42], q[31];
cswap q[30], q[41], q[42];
cx q[42], q[30];
cswap q[29], q[40], q[42];
cx q[42], q[29];
cswap q[28], q[39], q[42];
cx q[42], q[28];
cswap q[27], q[38], q[42];
cx q[42], q[27];
cx q[42], q[31];
cx q[42], q[30];
cx q[42], q[29];
cx q[42], q[28];
cx q[42], q[27];
cx q[42], q[41];
cx q[42], q[40];
cx q[42], q[39];
cx q[42], q[38];
ccx q[21], q[5], q[41];
ccx q[20], q[5], q[40];
ccx q[19], q[5], q[39];
ccx q[18], q[5], q[38];
ccx q[18], q[4], q[38];
ccx q[19], q[4], q[39];
ccx q[20], q[4], q[40];
ccx q[21], q[4], q[41];
cx q[42], q[38];
cx q[42], q[39];
cx q[42], q[40];
cx q[42], q[41];
cx q[42], q[26];
cx q[42], q[27];
cx q[42], q[28];
cx q[42], q[29];
cx q[42], q[30];
cx q[38], q[26];
cswap q[26], q[38], q[42];
cx q[39], q[27];
cswap q[27], q[39], q[42];
cx q[40], q[28];
cswap q[28], q[40], q[42];
cx q[41], q[29];
cswap q[29], q[41], q[42];
cx q[42], q[30];
cswap q[29], q[41], q[42];
cx q[42], q[29];
cswap q[28], q[40], q[42];
cx q[42], q[28];
cswap q[27], q[39], q[42];
cx q[42], q[27];
cswap q[26], q[38], q[42];
cx q[42], q[26];
cx q[42], q[30];
cx q[42], q[29];
cx q[42], q[28];
cx q[42], q[27];
cx q[42], q[26];
cx q[42], q[41];
cx q[42], q[40];
cx q[42], q[39];
cx q[42], q[38];
ccx q[21], q[4], q[41];
ccx q[20], q[4], q[40];
ccx q[19], q[4], q[39];
ccx q[18], q[4], q[38];
ccx q[10], q[3], q[38];
ccx q[11], q[3], q[39];
cx q[40], q[38];
cx q[40], q[39];
cx q[40], q[23];
cx q[40], q[24];
cx q[40], q[25];
cx q[38], q[23];
cswap q[23], q[38], q[40];
cx q[39], q[24];
cswap q[24], q[39], q[40];
cx q[40], q[25];
cswap q[24], q[39], q[40];
cx q[40], q[24];
cswap q[23], q[38], q[40];
cx q[40], q[23];
cx q[40], q[25];
cx q[40], q[24];
cx q[40], q[23];
cx q[40], q[39];
cx q[40], q[38];
ccx q[11], q[3], q[39];
ccx q[10], q[3], q[38];
ccx q[10], q[2], q[38];
ccx q[11], q[2], q[39];
cx q[40], q[38];
cx q[40], q[39];
cx q[40], q[22];
cx q[40], q[23];
cx q[40], q[24];
cx q[38], q[22];
cswap q[22], q[38], q[40];
cx q[39], q[23];
cswap q[23], q[39], q[40];
cx q[40], q[24];
cswap q[23], q[39], q[40];
cx q[40], q[23];
cswap q[22], q[38], q[40];
cx q[40], q[22];
cx q[40], q[24];
cx q[40], q[23];
cx q[40], q[22];
cx q[40], q[39];
cx q[40], q[38];
ccx q[11], q[2], q[39];
ccx q[10], q[2], q[38];
ccx q[8], q[1], q[38];
ccx q[9], q[1], q[39];
cx q[40], q[38];
cx q[40], q[39];
cx q[40], q[19];
cx q[40], q[20];
cx q[40], q[21];
cx q[38], q[19];
cswap q[19], q[38], q[40];
cx q[39], q[20];
cswap q[20], q[39], q[40];
cx q[40], q[21];
cswap q[20], q[39], q[40];
cx q[40], q[20];
cswap q[19], q[38], q[40];
cx q[40], q[19];
cx q[40], q[21];
cx q[40], q[20];
cx q[40], q[19];
cx q[40], q[39];
cx q[40], q[38];
ccx q[9], q[1], q[39];
ccx q[8], q[1], q[38];
ccx q[8], q[0], q[38];
ccx q[9], q[0], q[39];
cx q[40], q[38];
cx q[40], q[39];
cx q[40], q[18];
cx q[40], q[19];
cx q[40], q[20];
cx q[38], q[18];
cswap q[18], q[38], q[40];
cx q[39], q[19];
cswap q[19], q[39], q[40];
cx q[40], q[20];
cswap q[19], q[39], q[40];
cx q[40], q[19];
cswap q[18], q[38], q[40];
cx q[40], q[18];
cx q[40], q[20];
cx q[40], q[19];
cx q[40], q[18];
cx q[40], q[39];
cx q[40], q[38];
ccx q[9], q[0], q[39];
ccx q[8], q[0], q[38];
h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];
x q[0];
x q[1];
x q[2];
x q[3];
x q[4];
x q[5];
x q[6];
x q[7];
h q[38];
cp(-pi/4) q[0], q[38];
cx q[0], q[1];
cp(pi/4) q[1], q[38];
cx q[0], q[1];
cp(-pi/4) q[1], q[38];
cx q[1], q[2];
cp(pi/4) q[2], q[38];
cx q[0], q[2];
cp(-pi/4) q[2], q[38];
cx q[1], q[2];
cp(pi/4) q[2], q[38];
cx q[0], q[2];
cp(-pi/4) q[2], q[38];
h q[38];
h q[39];
cp(-pi/4) q[3], q[39];
cx q[3], q[4];
cp(pi/4) q[4], q[39];
cx q[3], q[4];
cp(-pi/4) q[4], q[39];
cx q[4], q[38];
cp(pi/4) q[38], q[39];
cx q[3], q[38];
cp(-pi/4) q[38], q[39];
cx q[4], q[38];
cp(pi/4) q[38], q[39];
cx q[3], q[38];
cp(-pi/4) q[38], q[39];
h q[39];
h q[40];
cp(-pi/4) q[5], q[40];
cx q[5], q[6];
cp(pi/4) q[6], q[40];
cx q[5], q[6];
cp(-pi/4) q[6], q[40];
cx q[6], q[39];
cp(pi/4) q[39], q[40];
cx q[5], q[39];
cp(-pi/4) q[39], q[40];
cx q[6], q[39];
cp(pi/4) q[39], q[40];
cx q[5], q[39];
cp(-pi/4) q[39], q[40];
h q[40];
cz q[40], q[7];
h q[40];
cp(-pi/4) q[39], q[40];
cx q[5], q[39];
cp(pi/4) q[39], q[40];
cx q[6], q[39];
cp(-pi/4) q[39], q[40];
cx q[5], q[39];
cp(pi/4) q[39], q[40];
cx q[6], q[39];
cp(-pi/4) q[6], q[40];
cx q[5], q[6];
cp(pi/4) q[6], q[40];
cx q[5], q[6];
cp(-pi/4) q[5], q[40];
h q[40];
h q[39];
cp(-pi/4) q[38], q[39];
cx q[3], q[38];
cp(pi/4) q[38], q[39];
cx q[4], q[38];
cp(-pi/4) q[38], q[39];
cx q[3], q[38];
cp(pi/4) q[38], q[39];
cx q[4], q[38];
cp(-pi/4) q[4], q[39];
cx q[3], q[4];
cp(pi/4) q[4], q[39];
cx q[3], q[4];
cp(-pi/4) q[3], q[39];
h q[39];
h q[38];
cp(-pi/4) q[2], q[38];
cx q[0], q[2];
cp(pi/4) q[2], q[38];
cx q[1], q[2];
cp(-pi/4) q[2], q[38];
cx q[0], q[2];
cp(pi/4) q[2], q[38];
cx q[1], q[2];
cp(-pi/4) q[1], q[38];
cx q[0], q[1];
cp(pi/4) q[1], q[38];
cx q[0], q[1];
cp(-pi/4) q[0], q[38];
h q[38];
x q[0];
x q[1];
x q[2];
x q[3];
x q[4];
x q[5];
x q[6];
x q[7];
h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[4] -> c[4];
measure q[5] -> c[5];
measure q[6] -> c[6];
measure q[7] -> c[7];