#!/usr/local/bin/perl

our $ourNodeCnt = int(<STDIN>);
our %ourNode;
for(my $c=0;$c<$ourNodeCnt;$c++){
	my $myStr = <STDIN>;
	my @myTemp = split(/\s+/,$myStr);
	$ourNode{$myTemp[0]}{l} = $myTemp[1];
	$ourNode{$myTemp[0]}{r} = $myTemp[2];
}

print "Node Count :  $ourNodeCnt\n";
foreach my $node (keys %ourNode){
	print "Node : $node , left : $ourNode{$node}{l} , right : $ourNode{$node}{r}\n";
}

goB("A");  print "\n";
goM("A");  print "\n";
goA("A");  print "\n";

sub goB {
	my $myNode = shift;

	print $myNode;
	if($ourNode{$myNode}{l} ne "\."){
		goB($ourNode{$myNode}{l});
	}
	if($ourNode{$myNode}{r} ne "\."){
		goB($ourNode{$myNode}{r});
	}
}


sub goM {
	my $myNode = shift;

	if($ourNode{$myNode}{l} ne "\."){
		goM($ourNode{$myNode}{l});
	}
	print $myNode;
	if($ourNode{$myNode}{r} ne "\."){
		goM($ourNode{$myNode}{r});
	}
}

sub goA {
	my $myNode = shift;

	if($ourNode{$myNode}{l} ne "\."){
		goA($ourNode{$myNode}{l});
	}
	if($ourNode{$myNode}{r} ne "\."){
		goA($ourNode{$myNode}{r});
	}
	print $myNode;
}
