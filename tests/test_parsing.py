from htmlishell.parsing import Parser


def test_ls_all():
    assert (
        Parser.parse(
            """<ls>
                   <all />
               </ls>
            """
        )
        == "ls --all"
    )


def test_ls_long():
    assert (
        Parser.parse(
            """<ls>
                 <l short=true />
               </ls>
            """
        )
        == "ls -l"
    )


def test_ls_all_long():
    assert (
        Parser.parse(
            """<ls>
                 <all />
                 <l short=true />
               </ls>
            """
        )
        == "ls --all -l"
    )
