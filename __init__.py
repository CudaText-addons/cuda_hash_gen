from cudatext import *

class Command:

    def callback_btn_close(self, id_dlg, id_ctl, data='', info=''):
        dlg_proc(id_dlg, DLG_HIDE, 0)
        dlg_proc(id_dlg, DLG_FREE, 0)

    def init_dlg(self):
        h=dlg_proc(0, DLG_CREATE)
        dlg_proc(h, DLG_PROP_SET, prop={'cap':'Hash Generator', 'w':600, 'h':390 })

        n=dlg_proc(h, DLG_CTL_ADD, 'button')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={'name': 'btn_close', 'cap':'Close', 'x':490, 'y':360, 'w':100,
          'on_change': self.callback_btn_close } )

        return h

    def dialog(self):
        self.h_dlg = self.init_dlg()
        dlg_proc(self.h_dlg, DLG_SHOW_NONMODAL)

