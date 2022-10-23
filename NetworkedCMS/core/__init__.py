import os
from flask import Flask
import typing as t


class NetworkedCMS(Flask):
    """A NetworkedCMS object acting as the Flask object which acts as the central object"""

    def __init__(self, import_name: str, static_url_path: t.Optional[str] = None,
                 static_folder: t.Optional[t.Union[str,
                                                   os.PathLike]] = "static",
                 static_host: t.Optional[str] = None, host_matching: bool = False, subdomain_matching: bool = False,
                 template_folder: t.Optional[str] = "templates", instance_path: t.Optional[str] = None, instance_relative_config: bool = False, 
                 root_path: t.Optional[str] = None):

        super().__init__(import_name, static_url_path, static_folder, static_host, host_matching, subdomain_matching, template_folder,
                         instance_path, instance_relative_config, root_path)

