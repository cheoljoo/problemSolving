#!/usr/local/bin/perl

our @arrBook;
our $ourCase = int(<STDIN>);
our $ourBook;
our $ourStore;
our @caseResult;
for(my $c=0;$c<$ourCase;$c++){
	$caseResult[$c] = 999999999999999;
	my $myStr = <STDIN>;
	my @myTemp = split(/\s+/,$myStr);
	$ourBook[$c] = int($myTemp[0]);
	$ourStore[$c] = int($myTemp[1]);
	for(my $i=0;$i<$ourBook[$c];$i++){
		my $myStr = <STDIN>;
		my @myPriceCoupon = split(/\s+/,$myStr);
		print "priceCoupon @myPriceCoupon \n";
		for(my $j=0;$j<$ourStore[$c];$j++){
			$arrBook[$c][$i][$j]{price} = $myPriceCoupon[$j*2];
			$arrBook[$c][$i][$j]{coupon} = $myPriceCoupon[$j*2+1];
		}
	}
}

print "case $ourCase\n";
for(my $c=0;$c<$ourCase;$c++){
	print "case $c book $ourBook[$c]\n";
	print "case $c store $ourStore[$c]\n";
}

for(my $c=0;$c<$ourCase;$c++){
	print "\nPrint [CASE $c]\n";
	for(my $i=0;$i<$ourBook[$c];$i++){
		print "$i    ";
		for(my $j=0;$j<$ourStore[$c];$j++){
			print "[$j] Price " . $arrBook[$c][$i][$j]{price} . " Coupon $arrBook[$c][$i][$j]{coupon}  |  ";
		}
		print "\n";
	}
}

our @cSum;
our @cCoupon;
for(my $c=0;$c<$ourCase;$c++){
	$cSum[$c] = 0;
	print "\n[CASE $c]\n";
	for(my $s=0;$s<$ourStore[$c];$s++){
		# goNext($c,next book depth ,current sum);	// current coupon
		$cCoupon[$c][$s] += $arrBook[$c][0][$s]{coupon};
		goNext($c,1,$arrBook[$c][0][$s]{price},"$s");
		$cCoupon[$c][$s] -= $arrBook[$c][0][$s]{coupon};
	}
	print ">>> Case $c Result = $caseResult[$c]  , List => $caseList[$c]\n";
}

sub goNext {
	my $myc = shift;
	my $mybook = shift;
	my $mysum = shift;
	my $mystorelist = shift;

	print "goNext => case : $myc , Depth Book : $mybook , mysum : $mysum , mystorelist : $mystorelist\ncCoupon : ";
	for(my $s=0;$s<$ourStore[$c];$s++){
		print " $cCoupon[$myc][$s] : ";
	}
	print "\n";

	if($mysum >= $caseResult[$myc]){
		print "SKIP case : $myc , mysum : $mysum , case Result : $caseResult[$myc] , list : $mystorelist\n";
		return ;
	}

	if( $mybook == $ourBook[$myc]){
		print "case : $myc , mysum : $mysum , case Result : $caseResult[$myc]\n";
		if($caseResult[$myc] > $mysum){
			$caseResult[$myc] = $mysum;
			$caseList[$myc] = $mystorelist;;
		}
		return ;
	}

	for(my $s=0;$s<$ourStore[$c];$s++){
		my $useCoupon = $cCoupon[$myc][$s] ;
		$cCoupon[$myc][$s] += ($arrBook[$myc][$mybook][$s]{coupon} - $useCoupon);
		my $mytmp = $mysum + $arrBook[$myc][$mybook][$s]{price} - $useCoupon;
		goNext($myc,$mybook+1,$mytmp,$mystorelist . "$s");
		$cCoupon[$myc][$s] -= ($arrBook[$myc][$mybook][$s]{coupon} - $useCoupon);
	}
}

