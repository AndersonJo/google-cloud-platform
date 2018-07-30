# -*- coding:utf-8 -*-

import argparse
import re
import sys

import apache_beam as beam
from apache_beam.io.textio import ReadFromText, WriteToText
from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions


def get_args():
    parser = argparse.ArgumentParser(sys.argv[1:])
    parser.add_argument('--input', default='gs://dataflow-samples/shakespeare/kinglear.txt')
    parser.add_argument('--output', default='gs://YOUR_BUCKET/DEST')
    known_args, pipeline_args = parser.parse_known_args()

    pipeline_args.extend([
        # 구글 클라우드 DataFlow에서 pipeline을 돌릴려면 `DataflowRunner` 로 바꿈
        # Spark에서 돌릴시 `SparkRunner` 로 바꿔줄수도 있음
        '--runner=DirectRunner',

        # Google Cloud Dataflow Service에서 실행시 Project ID 를 명시해줘야함
        # 예제) anderson-1189
        '--project=YOUR_PROJECT_ID',

        # Google Cloud Dataflow Service에서 실행시 Local file을 stagning시키기 위해서 필요
        '--staging_location={0}/staging'.format(known_args.output),

        # Google Cloud Dataflow Service에서 실행시 temporary파일을 위해서 필요
        '--temp_location={0}/temp'.format(known_args.output),

        # Job 이름 설정
        'job_name=wordcount_job'
    ])

    print(known_args)
    print(pipeline_args)

    return known_args, pipeline_args


def main():
    args, pipeline_args = get_args()

    # 먼저 PipelineOpions 을 통해서 pipeline에 대한 설정을 할 수 있습니다.
    # 예를 들어서 pipeline runner를 설정하여 무엇이 pipeline을 실행할지 설정할수 있습니다.

    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=pipeline_options) as p:
        # Input data file -> TextIO.Read Transform -> PCollection(lines)
        lines = p | ReadFromText(args.input)

        counts = (
                lines
                | 'Split' >> (beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x))
                              .with_output_types(unicode))
                | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
                | 'GroupAndSum' >> beam.CombinePerKey(sum))

        # Format the counts into a PCollection of strings.
        def format_result(word_count):
            (word, count) = word_count
            return '%s: %s' % (word, count)

        output = counts | 'Format' >> beam.Map(format_result)

        # Write the output using a "Write" transform that has side effects.
        # pylint: disable=expression-not-assigned
        output | WriteToText(args.output)


if __name__ == '__main__':
    main()
