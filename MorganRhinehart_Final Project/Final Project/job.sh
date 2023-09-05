#!/bin/bash
#SBATCH --job-name="Final_EOS"
#SBATCH -n 4
#SBATCH -p genacc_q
##SBATCH --mail-type="ALL"
#SBATCH -t 48:00:00


export PATH=$PATH:/gpfs/research/ouyanggroup/CHM5580/VASP_Binary

module load intel/21
module load mvapich2/2.3.5

rm WAVECAR
for i in 3.46 3.56 3.66 3.76 3.86 3.96 4.06 4.16 4.26
do
    cat > POSCAR << !
Ni4
1.0
   3.5057980000000000    0.0000000000000000    0.0000000000000002
   0.0000000000000006    3.5057980000000000    0.0000000000000002
   0.0000000000000000    0.0000000000000000    3.5057980000000000
Ni
4
direct
   0.0000000000000000    0.0000000000000000    0.0000000000000000 Ni
   0.0000000000000000    0.5000000000000000    0.5000000000000000 Ni
   0.5000000000000000    0.0000000000000000    0.5000000000000000 Ni
   0.5000000000000000    0.5000000000000000    0.0000000000000000 Ni
!

    printf "Run for a=${i}\n"
    srun -n 4 vasp_std >> vasp.out;
    E=`grep E0 OSZICAR | tail -1 | awk '{print $5}'`
    volume=`grep volume OUTCAR | tail -1 | awk '{printf $5}'`
    echo ${volume} $E >> Summary.fcc
    cp POSCAR POSCAR_${i};
    cp OSZICAR OSZICAR_${i};
    cp OUTCAR OUTCAR_${i};
    cp CONTCAR CONTCAR_${i};
done

