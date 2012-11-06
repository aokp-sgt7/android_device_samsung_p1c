#
# Copyright (C) 2008 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, sys

LOCAL_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
RELEASETOOLS_DIR = os.path.abspath(os.path.join(LOCAL_DIR, '../../../build/tools/releasetools'))

import edify_generator

class EdifyGenerator(edify_generator.EdifyGenerator):
    def AssertDevice(self, device):
      edify_generator.EdifyGenerator.AssertDevice(self, device)
      self.script.append('ui_print("");')
      self.script.append('ui_print("            ,,cSS$");')
      self.script.append('ui_print("            $$$$$$    ,,ccc,,    ,,cSS$   ,c$$$$SScc,");')
      self.script.append('ui_print("    ,ccS$$$$$$$$$$ ,cS$$$$$$$Sc, $$$$$$  ,S$$$S$$$$$$$$$SScc,");')
      self.script.append('ui_print("   ;$$$$$*`*$$$$$$;$$$$$*`*$$$$$;$$$$$$,cS$$$*`$$$$$$*`l$$$$$;");')
      self.script.append('ui_print("  ;l$$$$l   $$$$$$l$$$$$   $$$$$l$$$$$$$$$S*`  $$$$$$  ;$$$$$l");')
      self.script.append('ui_print("  l$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$Scc,, $$$$$$  ;$$$$$l");')
      self.script.append('ui_print("  $$$$$$    $$$$$$$$$$$$   $$$$$$$$$$$$`l$$$Sc,$$$$$$c,l$$$$$;");')
      self.script.append('ui_print("  $$$$$$;   $$$$$$l$$$$$   $$$$$l$$$$$$ ;$$$$$$$$$$$$$$$SS**`");')
      self.script.append('ui_print("  l$$$$$l   $$$$$$;$$$$$c,c$$$$$;$$$$$$  $$$$$$$$$$$$");')
      self.script.append('ui_print("  ;$$$$$$;  `*S$$$ `*S$$$$$$$S*` $$$$$$  $$$$$$$$$$$$");')
      self.script.append('ui_print("   l$$$$$l            ``***``    $$S**`  $$$$$$`*S$$$");')
      self.script.append('ui_print("-- ;S**``  ----------------------------- `**S$$ ------- --- -");')
      self.script.append('ui_print(";;[ . . A O K P - S G T 7 ];;; ,c$$$$*`,cS$$Sc,*$$$$$*,c$$$c,");')
      self.script.append('ui_print(";;[ ;;;;;;;;; by stimpz0r ];;; $$; ;;; $$ ;; $$  $$ ;;;;;;`$$");')
      self.script.append('ui_print(";;[                       ];;;,`*$$$Sc,*$,,,,$$  $$ ;;;;;; $$");')
      self.script.append('ui_print(";;[  ** CDMA ** JELLYBEAN ];;;``    ;$$ `````$$  $$ ;;;;;; $$");')
      self.script.append('ui_print(";;[   (SCH-I800/SPH-P100) ];;;,`*$$$$*`ccS$$$*`, $$ ;;;;;; $$");')
      self.script.append('ui_print("- --- ---------------------------------------------------- *$");')
      self.script.append('ui_print("(::) AOKP (Android Open Kang Project) by TeamKang");')
      self.script.append('ui_print("(::) SGT7 device/vendor/kernel by SGT7 ICS TE4M");')
      self.script.append('ui_print("(::) built and SGT7 components AOKPerized by stimpz0r");')
      self.script.append('ui_print("---------------------------------------------------- --- -- -");')
      self.script.append('ui_print("");')
      self.script.append('ui_print("(::) extracting needed files for installation...");')
      self.script.append('show_progress(0.15, 5);');
      self.script.append(
            ('package_extract_file("updater.sh", "/tmp/updater.sh");\n'
             'set_perm(0, 0, 0777, "/tmp/updater.sh");'))
      self.script.append(
           ('package_extract_file("make_ext4fs", "/tmp/make_ext4fs");\n'
            'set_perm(0, 0, 0777, "/tmp/make_ext4fs");'))
      self.script.append(
            ('package_extract_file("busybox", "/tmp/busybox");\n'
             'set_perm(0, 0, 0777, "/tmp/busybox");'))
      self.script.append(
            ('package_extract_file("flash_image", "/tmp/flash_image");\n'
             'set_perm(0, 0, 0777, "/tmp/flash_image");'))
      self.script.append(
            ('package_extract_file("erase_image", "/tmp/erase_image");\n'
             'set_perm(0, 0, 0777, "/tmp/erase_image");'))
      self.script.append(
            ('package_extract_file("bml_over_mtd", "/tmp/bml_over_mtd");\n'
             'set_perm(0, 0, 0777, "/tmp/bml_over_mtd");'))
      self.script.append(
            ('package_extract_file("bml_over_mtd.sh", "/tmp/bml_over_mtd.sh");\n'
             'set_perm(0, 0, 0777, "/tmp/bml_over_mtd.sh");'))

      self.script.append('ui_print("(::) extracting kernel...");')
      self.script.append('package_extract_file("boot.img", "/tmp/boot.img");')
      self.script.append('ui_print("(::) checking state of BML/MTD and flashing kernel...");')
      self.script.append('assert(run_program("/tmp/updater.sh", "cdma") == 0);')
      self.script.append('ui_print("(::) installing system...");')

    def RunBackup(self, command):
      edify_generator.EdifyGenerator.RunBackup(self, command)

    def RunConfig(self, command):
      edify_generator.EdifyGenerator.RunConfig(self, command)

    def WriteBMLoverMTD(self, partition, partition_start_block, reservoirpartition, reservoir_start_block, image):
      """Write the given package file into the given partition."""

      args = {'partition': partition, 'partition_start_block': partition_start_block, 'reservoirpartition': reservoirpartition, 'reservoir_start_block': reservoir_start_block, 'image': image}

      self.script.append(
            ('assert(run_program("/tmp/erase_image", "%(partition)s"));') % args)

      self.script.append(
            ('assert(package_extract_file("%(image)s", "/tmp/%(partition)s.img"),\n'
             '       run_program("/tmp/bml_over_mtd.sh", "%(partition)s", "%(partition_start_block)s", "%(reservoirpartition)s", "%(reservoir_start_block)s", "/tmp/%(partition)s.img"),\n'
             '       delete("/tmp/%(partition)s.img"));') % args)

