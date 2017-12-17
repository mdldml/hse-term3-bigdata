Two consecutive MapReduce jobs are used for solving the task (mapper.py + reducer.py and mapper2.py + reducer2.py).

Local run:

    cat star2002-sample.csv | python mapper.py | sort -k 1,1 | python reducer.py > quantiles.txt
    cat star2002-sample.csv | python mapper2.py | sort -k 1,1 | python reducer2.py > result.txt

To test on Hadoop locally, pool and run:

    docker pull sequenceiq/hadoop-docker:2.7.1
    docker run -it sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash
    cd $HADOOP_PREFIX

Go to other terminal and copy files into docker:

    for f in mapper.py mapper2.py reducer.py reducer2.py star2002-sample.csv; do docker cp $f <your container name>:/usr/local/; done

Go back to hadoop docker:

    bin/hdfs dfs -mkdir input_data
    bin/hdfs dfs -put star2002-sample.csv input_data

    bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input input_data -output quantiles -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py
    bin/hdfs dfs -getmerge quantiles quantiles.txt

    bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input input_data -output result -mapper mapper2.py -reducer reducer2.py -file mapper2.py -file reducer2.py -file quantiles.txt
    bin/hdfs dfs -getmerge result result.txt

Results can be seen in result.txt file.
