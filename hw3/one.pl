#!/usr/bin/perl -n
#Kevin Hsieh 861054367

BEGIN{ open($file, "+>>", "hourlyinfo") }

(my $month, my $day, $time) = split(' ', $_);
(my $hour, my $min, my $second) = split(':',$time);

$rejects{$min}++ if /postfix.*reject/;
$quarantines{$min}++ if /amavis/;

END{
    for $k (sort keys %rejects){
	print $file "$month $day $hour:$k [postfix rejects:$rejects{$k}] [amavis quarantines:$quarantines{$k}]\n"
    }
}
