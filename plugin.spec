# pluging type can be install,provision,other
plugin_type: other
subparsers:
    # the actual name of the plugin
    simple-plugin:
        description: This is a simple demo plugin
        include_groups: ["Ansible options", "Common options"]
        groups:
            - title: Option group.
              options:
                  option1:
                      type: Value
                      help: Simple option with default value
                      default: foo
                  flag:
                      type: Bool
                      default: False

