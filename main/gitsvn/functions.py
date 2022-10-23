import csv
from pathlib import Path

from main.gitsvn.models import ProjectDetail
from main.utility.functions import LoggingService

log = LoggingService()


class CVSImporter:
    def __init__(self):
        self.read_csv()

    def read_csv(self):
        filename = "/home/linux/workspace/git/gitlabcli/export.csv"
        if Path(filename).exists():
            log.debug(f"File path exists: {filename}")
            csv_arr = list()
            ProjectDetail.objects.all().delete()
            log.debug("ProjectDetail deleted!")

            with open(file=filename, encoding="utf-8", mode="r") as csvf:
                try:
                    csv_arr = csv.DictReader(csvf)
                    list_of_dict = list(csv_arr)
                    objs = [
                        ProjectDetail(
                            name=row["name"],
                            project_id=row["id"],
                            url=row["web_url"],
                            git="gitlab",
                            namespace=row["namespace"],
                            default_branch=row["default_branch"],
                            ssh_url_to_repo=row["ssh_url_to_repo"],
                        )
                        for row in list_of_dict
                    ]
                    ProjectDetail.objects.bulk_create(objs)
                    log.info("Data inserted.")
                except Exception as e:
                    log.error(e)
